from mslm_email_verify import EmailVerify
from mslm_otp import Otp


class Mslm:
    """
    Central service orchestrating and facilitating access to other services within the Mslm.

    Attributes:-
        - mslm_email_verify (EmailVerify): Instance of the EmailVerify service.
        - mslm_otp (Otp): Instance of the Otp service.

    Methods:-
        - __init__(self, api_key:str): Constructor method to initialize Mslm object.
        - set_http_client(self, http_client): Sets the HTTP client for all services.
        - set_base_url(self, base_url_str): Sets the base URL for all services.
        - set_user_agent(self, user_agent): Sets the user agent for all services.
        - set_api_key(self, api_key): Sets the API key for all services.
    """

    def __init__(self, api_key: str):
        """
        Initializes a Mslm object with instances of EmailVerify, Otp, and Lib services.

        Parameters:-
            - api_key (str): The API key used for authentication.
        """
        self.email_verify = EmailVerify(api_key)
        self.otp = Otp(api_key)
