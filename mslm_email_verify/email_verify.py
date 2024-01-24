import json

from mslm_lib.lib import Lib
from mslm_lib.req_opts import ReqOpts
from mslm_lib.mslm_errors import MslmError, RequestQuotaExceededError
from .single_verify_resp import SingleVerifyResp


class EmailVerify:
    """
    Class for performing email verification using an API.

    Attributes:-
        - _lib (Lib): Instance of the Lib utility for handling HTTP requests and responses.

    Note:
    The '_lib' attribute is considered private and should not be accessed directly from outside the class.

    Methods:-
        - __init__(self, api_key:str=None): Initializes an EmailVerify object with an API key.
        - set_http_client(self, http_client): Sets the HTTP client to be used for making requests.
        - set_user_agent(self, user_agent): Sets the user agent to be used in HTTP requests.
        - set_api_key(self, api_key): Sets the API key for authentication.
        - single_verify(self, email:str, opts:SingleVerifyReqOpts=None)-> (SingleVerifyResp, Error): Performs a single email verification with optional request options.

    Usage:-
        email_verifier = EmailVerify(api_key="your_api_key")
        ev_resp, ev_err = email_verifier.single_verify("example@example.com")

        # Using custom request options
        opts = email_verifier.SingleVerifyReqOpts.Builder().with_disable_url_encode(True).build()
        ev_resp, ev_err = email_verifier.single_verify("example@example.com", opts)
    """

    def __init__(self, api_key: str):
        """
        Initializes an EmailVerify object with an API key.

        Parameters:-
            - api_key (str): The API key used for authentication.
        """
        self._lib = Lib(api_key)  # Private attribute

    def set_http_client(self, http_client):
        """
        Sets the HTTP client to be used for making requests.

        Parameters:-
            - http_client: The HTTP client object.
        """
        self._lib.set_http_client(http_client)

    def set_user_agent(self, user_agent):
        """
        Sets the user agent to be used in HTTP requests.

        Parameters:-
            - user_agent (str): The user agent string.
        """
        self._lib.set_user_agent(user_agent)

    def set_api_key(self, api_key: str):
        """
        Sets the API key for authentication.

        Parameters:-
            - api_key (str): The API key used for authentication.
        """
        self._lib.set_api_key(api_key)

    def single_verify(
        self, email: str, opts: ReqOpts = None
    ) -> (SingleVerifyResp, MslmError):
        """
        Performs a single email verification with optional request options.

        Parameters:-
            - email (str): The email address to be verified.
            - opts (ReqOpts): Optional request options for customization.

        Returns:-
            - SingleVerifyResp: An object representing the response of the email verification.
            - Exception: An object representing and error during the API request.
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

        qp = {"email": email}

        t_url = self._lib.prepare_url("/api/sv/v1", qp, opt)
        resp = self._lib.req_and_resp(t_url, opt)
        resp_data = json.loads(resp.text)

        status_code = resp.status_code
        if status_code == 429:
            return None, RequestQuotaExceededError()
        if status_code != 200:
            return None, MslmError(status_code, "API request failed")

        return SingleVerifyResp(**resp_data), None
