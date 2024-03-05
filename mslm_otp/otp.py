import json

from mslm_lib.lib import Lib
from mslm_lib.req_opts import ReqOpts
from mslm_lib.mslm_errors import MslmError, RequestQuotaExceededError
from .otp_send_req import OtpSendReq
from .otp_resp import OtpSendResp, OtpTokenVerifyResp
from .otp_token_verify_req import OtpTokenVerifyReq


class Otp:
    """
    Service class for handling OTP (One-Time Password).

    Attributes:-
        - _lib (Lib): Instance of the Lib utility for handling HTTP requests and responses.

    Note:
    The '_lib' attribute is considered private and should not be accessed directly from outside the class.

    Methods:-
        - __init__(self, api_key=None): Constructor method to initialize Otp object.
        - set_http_client(self, http_client): Sets the HTTP client for the Otp service.
        - set_user_agent(self, user_agent): Sets the user agent for the Otp service.
        - set_api_key(self, api_key): Sets the API key for the Otp service.
        - send(self, otp_req: OtpSendReq)-> (OtpSendResp, Error): Sends an OTP using the provided OTP request and optional custom options.
        - verify(self, otp_token_req: OtpTokenVerifyReq, opts: OtpReqOpts = None) -> (OtpTokenVerifyResp, Error): Verifies an OTP token with optional custom options.

    Usage:-
        o = Otp(api_key="your_api_key")
        otp_req = o.OtpReq(phone="1234567890", tmpl_sms="Your OTP is: {mslm_otp}", token_len=6, expire_seconds=300)
        otp_resp, otp_err = o.send(otp_req)

        # Using custom request options
        opts = o.OtpReqOpts.Builder().with_disable_url_encode(True).build()
        otp_resp, otp_err = o.send(otp_req, opts)
    """

    def __init__(self, api_key=None):
        """
        Initializes an Otp object with an optional API key.

        Parameters:-
            - api_key (str): The API key used for authentication (optional).
        """

        self._lib = Lib(api_key)  # Private attribute

    def set_http_client(self, http_client):
        """
        Sets the HTTP client for the Otp service.

        Parameters:-
            - http_client: The HTTP client to be set for the Otp service.
        """
        self._lib.set_http_client(http_client)

    def set_user_agent(self, user_agent):
        """
        Sets the user agent for the Otp service.

        Parameters:-
            - user_agent (str): The user agent to be set for the Otp service.
        """
        self._lib.set_user_agent(user_agent)

    def set_api_key(self, api_key):
        """
        Sets the API key for the Otp service.

        Parameters:-
            - api_key (str): The API key to be set for the Otp service.
        """
        self._lib.set_api_key(api_key)

    def send(
        self, otp_req: OtpSendReq, opts: ReqOpts = None
    ) -> (OtpSendResp, MslmError):
        """
        Sends an OTP with custom options.

        Parameters:-
            - otp_req (OtpReq): The OTP request containing details for sending OTP.
            - opts (ReqOpts): Custom options for the OTP sending operation (optional).

        Returns:-
            - OtpSendResp: An object representing the response of the OTP sending operation.
            - Error: An object representing the error response of the OTP sending operation.
        """

        opt = (
            ReqOpts.Builder()
            .with_api_key(self._lib.api_key)
            .with_base_url(self._lib.base_url)
            .with_http_client(self._lib.http)
            .with_user_agent(self._lib.user_agent)
            .build()
        )

        if opts:
            opt = opts

        qp = {
            "phone": otp_req.phone,
            "tmpl_sms": otp_req.tmpl_sms,
            "token_len": otp_req.token_len,
            "expire_seconds": otp_req.expire_seconds,
        }

        t_url = self._lib.prepare_url("/api/mslm_otp/v1/send", qp, opt)
        resp = self._lib.req_and_resp(t_url, opt, method="POST", data=qp)
        resp_data = json.loads(resp.text)

        status_code = resp.status_code
        if status_code == 429:
            return None, RequestQuotaExceededError()
        if status_code != 200:
            return None, MslmError(
                status_code, resp_data.get("msg", "API request failed")
            )

        return OtpSendResp(**resp_data), None

    def verify(
        self, otp_token_req: OtpTokenVerifyReq, opts: ReqOpts = None
    ) -> (OtpTokenVerifyResp, MslmError):
        """
        Verifies an OTP token with optional custom options.

        Parameters:-
            - otp_token_req (OtpTokenVerifyReq): The OTP token verification request.
            - opts (ReqOpts): Custom options for the OTP token verification operation (optional).
        Returns:-
            - OtpResp: An object representing the response of the OTP token verification operation.
            - Error: An object representing the error response of the OTP token verification operation.
        """
        opt = (
            ReqOpts.Builder()
            .with_api_key(self._lib.api_key)
            .with_base_url(self._lib.base_url)
            .with_http_client(self._lib.http)
            .with_user_agent(self._lib.user_agent)
            .build()
        )

        if opts:
            opt = opts

        qp = {
            "phone": otp_token_req.phone,
            "token": otp_token_req.token,
            "consume": otp_token_req.consume,
        }

        t_url = self._lib.prepare_url("/api/mslm_otp/v1/token_verify", qp, opt)
        resp = self._lib.req_and_resp(t_url, opt, method="POST", data=qp)
        resp_data = json.loads(resp.text)

        status_code = resp.status_code
        if status_code == 429:
            return None, RequestQuotaExceededError()
        if status_code != 200:
            return None, MslmError(
                status_code, resp_data.get("msg", "API request failed")
            )

        return OtpTokenVerifyResp(**resp_data), None
