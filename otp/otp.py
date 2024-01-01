import json
from lib import Lib
from lib.req_opts import ReqOpts
from otp.otp_req import OtpReq
from otp.otp_req_opts import OtpReqOpts
from otp.otp_resp import OtpResp


class Otp:
    """
    Service class for handling OTP (One-Time Password).

    Attributes:-
        - lib (Lib): Instance of the Lib utility for handling HTTP requests and responses.

    Methods:-
        - __init__(self, api_key=None): Constructor method to initialize Otp object.
        - set_http_client(self, http_client): Sets the HTTP client for the Otp service.
        - set_base_url(self, base_url_str): Sets the base URL for the Otp service.
        - set_user_agent(self, user_agent): Sets the user agent for the Otp service.
        - set_api_key(self, api_key): Sets the API key for the Otp service.
        - send_otp(self, otp_req: OtpReq): Sends an OTP using the provided OTP request.
        - send_otp_with_opts(self, otp_req: OtpReq, opts=None): Sends an OTP with custom options.
    """

    def __init__(self, api_key=None):
        """
        Initializes an Otp object with an optional API key.

        Parameters:-
            - api_key (str): The API key used for authentication (optional).
        """
        self.lib = Lib(api_key)

    def set_http_client(self, http_client):
        """
        Sets the HTTP client for the Otp service.

        Parameters:-
            - http_client: The HTTP client to be set for the Otp service.
        """
        self.lib.set_http_client(http_client)

    def set_base_url(self, base_url_str):
        """
        Sets the base URL for the Otp service.

        Parameters:-
            - base_url_str (str): The base URL to be set for the Otp service.
        """
        self.lib.set_base_url(base_url_str)

    def set_user_agent(self, user_agent):
        """
        Sets the user agent for the Otp service.

        Parameters:-
            - user_agent (str): The user agent to be set for the Otp service.
        """
        self.lib.set_user_agent(user_agent)

    def set_api_key(self, api_key):
        """
        Sets the API key for the Otp service.

        Parameters:-
            - api_key (str): The API key to be set for the Otp service.
        """
        self.lib.set_api_key(api_key)

    def send_otp(self, otp_req: OtpReq):
        """
        Sends an OTP using the provided OTP request.

        Parameters:-
            - otp_req (OtpReq): The OTP request containing details for sending OTP.

        Returns:
            - OtpResp: An object representing the response of the OTP sending operation.
        """
        opt = OtpReqOpts.Builder().with_req_opts(
            ReqOpts.Builder()
            .with_api_key(self.lib.api_key)
            .with_base_url(self.lib.base_url)
            .with_http_client(self.lib.http)
            .with_user_agent(self.lib.user_agent)
            .build()
        ).build()

        qp = {
            "phone": otp_req.phone,
            "tmpl_sms": otp_req.tmpl_sms,
            "token_len": otp_req.token_len,
            "expire_seconds": otp_req.expire_seconds
        }

        t_url = self.lib.prepare_url("/api/otp/v1/send", qp, opt.req_opts)
        resp = self.lib.req_and_resp(t_url, opt.req_opts, method='POST', data=qp)

        return OtpResp(**json.loads(resp))

    def send_otp_with_opts(self, otp_req: OtpReq, opts=None):
        """
        Sends an OTP with custom options.

        Parameters:-
            - otp_req (OtpReq): The OTP request containing details for sending OTP.
            - opts: Custom options for the OTP sending operation (optional).

        Returns:
            - OtpResp: An object representing the response of the OTP sending operation.
        """
        opt = OtpReqOpts.Builder().with_req_opts(
            ReqOpts.Builder().build()
        ).build()

        if opts:
            opt = opts

        qp = {
            "phone": otp_req.phone,
            "tmpl_sms": otp_req.tmpl_sms,
            "token_len": otp_req.token_len,
            "expire_seconds": otp_req.expire_seconds
        }

        t_url = self.lib.prepare_url("/api/otp/v1/send", qp, opt.req_opts)
        resp = self.lib.req_and_resp(t_url, opt.req_opts, method='POST', data=qp)

        return OtpResp(**json.loads(resp))
