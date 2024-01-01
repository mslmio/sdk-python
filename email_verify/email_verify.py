import json

from urllib.parse import urlencode
from lib import Lib
from lib.req_opts import ReqOpts

from .single_verify_resp import SingleVerifyResp
from .single_verify_req_opts import SingleVerifyReqOpts


class EmailVerify:
    """
    Class for performing email verification using an API.

    Attributes:-
        - lib (Lib): The underlying library for making API requests.

    Methods:-
        - __init__(self, api_key=None): Initializes an EmailVerify object with an optional API key.
        - set_http_client(self, http_client): Sets the HTTP client to be used for making requests.
        - set_base_url(self, base_url_str): Sets the base URL for API requests.
        - set_user_agent(self, user_agent): Sets the user agent to be used in HTTP requests.
        - set_api_key(self, api_key): Sets the API key for authentication.
        - single_verify(self, email): Performs a single email verification using the specified email address.
        - single_verify_with_opts(self, email, opts=None): Performs a single email verification with optional request options.

    Usage:-
        email_verifier = EmailVerify(api_key="your_api_key")
        email_verifier.single_verify("example@example.com")
    """

    def __init__(self, api_key=None):
        """
        Initializes an EmailVerify object with an optional API key.

        Parameters:-
            - api_key (str): The API key used for authentication.
        """
        self.lib = Lib(api_key)

    def set_http_client(self, http_client):
        """
        Sets the HTTP client to be used for making requests.

        Parameters:-
            - http_client: The HTTP client object.
        """
        self.lib.set_http_client(http_client)

    def set_base_url(self, base_url_str):
        """
        Sets the base URL for API requests.

        Parameters:-
            - base_url_str (str): The base URL for API requests.
        """
        self.lib.set_base_url(base_url_str)

    def set_user_agent(self, user_agent):
        """
        Sets the user agent to be used in HTTP requests.

        Parameters:-
            - user_agent (str): The user agent string.
        """
        self.lib.set_user_agent(user_agent)

    def set_api_key(self, api_key):
        """
        Sets the API key for authentication.

        Parameters:-
            - api_key (str): The API key used for authentication.
        """
        self.lib.set_api_key(api_key)

    def single_verify(self, email):
        """
        Performs a single email verification using the specified email address.

        Parameters:-
            - email (str): The email address to be verified.

        Returns:
            - SingleVerifyResp: An object representing the response of the email verification.
        """
        opt = SingleVerifyReqOpts.Builder().with_req_opts(
            ReqOpts.Builder()
            .with_api_key(self.lib.api_key)
            .with_base_url(self.lib.base_url)
            .with_http_client(self.lib.http)
            .with_user_agent(self.lib.user_agent)
            .build()
        ).build()

        qp = {"email": email}

        t_url = self.lib.prepare_url("/api/sv/v1", qp, opt.req_opts)
        resp = self.lib.req_and_resp(t_url, opt.req_opts)

        return SingleVerifyResp(**json.loads(resp))

    def single_verify_with_opts(self, email, opts=None):
        """
        Performs a single email verification with optional request options.

        Parameters:-
            - email (str): The email address to be verified.
            - opts (SingleVerifyReqOpts): Optional request options for customization.

        Returns:
            - SingleVerifyResp: An object representing the response of the email verification.
        """
        opt = SingleVerifyReqOpts.Builder().with_req_opts(
            ReqOpts.Builder().build()
        ).build()

        if opts:
            opt = opts

        if opt.disable_url_encode is not None and not opt.disable_url_encode:
            email = urlencode({"email": email})[6:]

        qp = {"email": email}

        t_url = self.lib.prepare_url("/api/sv/v1", qp, opt.req_opts)
        resp = self.lib.req_and_resp(t_url, opt.req_opts)

        return SingleVerifyResp(**json.loads(resp))
