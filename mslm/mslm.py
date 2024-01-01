from email_verify import EmailVerify
from lib import Lib
from otp import Otp


class Mslm:
    """
    Central service orchestrating and facilitating access to other services within the Mslm.

    Attributes:-
        - email_verify (EmailVerify): Instance of the EmailVerify service.
        - otp (Otp): Instance of the Otp service.
        - lib (Lib): Instance of the Lib utility for handling HTTP requests and responses.

    Methods:-
        - __init__(self, api_key=None): Constructor method to initialize Mslm object.
        - set_http_client(self, http_client): Sets the HTTP client for all services.
        - set_base_url(self, base_url_str): Sets the base URL for all services.
        - set_user_agent(self, user_agent): Sets the user agent for all services.
        - set_api_key(self, api_key): Sets the API key for all services.
    """

    def __init__(self, api_key=None):
        """
        Initializes a Mslm object with instances of EmailVerify, Otp, and Lib services.

        Parameters:-
            - api_key (str): The API key used for authentication (optional).
        """
        self.email_verify = EmailVerify(api_key)
        self.otp = Otp(api_key)
        self.lib = Lib(api_key)

    def set_http_client(self, http_client):
        """
        Sets the HTTP client for all services.

        Parameters:-
            - http_client: The HTTP client to be set for all services.
        """
        # For simplicity, assume http_client is a requests.Session object
        self.lib.set_http_client(http_client)
        self.otp.set_http_client(http_client)
        self.email_verify.set_http_client(http_client)

    def set_base_url(self, base_url_str):
        """
        Sets the base URL for all services.

        Parameters:-
            - base_url_str (str): The base URL to be set for all services.
        """
        self.lib.set_base_url(base_url_str)
        self.otp.set_base_url(base_url_str)
        self.email_verify.set_base_url(base_url_str)

    def set_user_agent(self, user_agent):
        """
        Sets the user agent for all services.

        Parameters:-
            - user_agent (str): The user agent to be set for all services.
        """
        self.lib.set_user_agent(user_agent)
        self.otp.set_user_agent(user_agent)
        self.email_verify.set_user_agent(user_agent)

    def set_api_key(self, api_key):
        """
        Sets the API key for all services.

        Parameters:-
            - api_key (str): The API key to be set for all services.
        """
        self.lib.set_api_key(api_key)
        self.otp.set_api_key(api_key)
        self.email_verify.set_api_key(api_key)
