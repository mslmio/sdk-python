from urllib.parse import urlparse, urlunparse, ParseResult
from requests import Session


class ReqOpts:
    """
    Request options class for configuring HTTP requests.

    Attributes:-
        - api_key (str): The API key used for authentication.
        - http (Session): The HTTP session object for making requests.
        - base_url (ParseResult): Parsed URL for the base endpoint of the API.
        - user_agent (str): The user agent string used in HTTP headers.

    Methods:-
        - __init__(self, api_key="", http=None, base_url="https://mslm.io", user_agent="mslm"): Constructor method.
        - get_api_key(self): Returns the API key.
        - get_http_client(self): Returns the HTTP client.
        - get_base_url(self): Returns the parsed base URL.
        - get_user_agent(self): Returns the user agent string.

        - Builder: Nested builder class for constructing instances of ReqOpts.
    """

    def __init__(
        self,
        api_key="",
        http=None,
        base_url="https://mslm.io",
        user_agent="mslm",
    ):
        """
        Initializes a ReqOpts object with default or provided values.

        Parameters:-
            - api_key (str): The API key used for authentication.
            - http (Session): The HTTP session object for making requests.
            - base_url (str or ParseResult): The base URL for API requests.
            - user_agent (str): The user agent string.
        """
        self.api_key = api_key
        self.http = http if http else Session()
        self.base_url = urlparse(base_url)
        self.user_agent = user_agent

    def get_api_key(self):
        """
        Returns the API key.

        Returns:
            - str: The API key.
        """
        return self.api_key

    def get_http_client(self):
        """
        Returns the HTTP client.

        Returns:
            - Session: The HTTP client.
        """
        return self.http

    def get_base_url(self):
        """
        Returns the parsed base URL.

        Returns:
            - ParseResult: The parsed base URL.
        """
        return self.base_url

    def get_user_agent(self):
        """
        Returns the user agent string.

        Returns:
            - str: The user agent string.
        """
        return self.user_agent

    class Builder:
        """
        Builder class for constructing instances of ReqOpts.

        Methods:-
            - with_api_key(self, api_key): Sets the API key.
            - with_http_client(self, http): Sets the HTTP client.
            - with_base_url(self, base_url): Sets the base URL.
            - with_user_agent(self, user_agent): Sets the user agent.
            - build(self): Builds and returns an instance of ReqOpts.
        """

        def __init__(self):
            self.opts = ReqOpts()

        def with_api_key(self, api_key):
            """
            Sets the API key.

            Parameters:-
                - api_key (str): The API key.

            Returns:
                - Builder: The builder object for method chaining.
            """
            self.opts.api_key = api_key
            return self

        def with_http_client(self, http):
            """
            Sets the HTTP client.

            Parameters:-
                - http (Session): The HTTP client.

            Returns:
                - Builder: The builder object for method chaining.
            """
            self.opts.http = http
            return self

        def with_base_url(self, base_url):
            """
            Sets the base URL.

            Parameters:-
                - base_url (str or ParseResult): The base URL.

            Returns:
                - Builder: The builder object for method chaining.
            """
            if isinstance(base_url, ParseResult):
                base_url = urlunparse(base_url)
            self.opts.base_url = base_url
            return self

        def with_user_agent(self, user_agent):
            """
            Sets the user agent.

            Parameters:-
                - user_agent (str): The user agent string.

            Returns:
                - Builder: The builder object for method chaining.
            """
            self.opts.user_agent = user_agent
            return self

        def build(self):
            """
            Builds and returns an instance of ReqOpts.

            Returns:
                - ReqOpts: An instance of ReqOpts with the specified options.
            """
            return self.opts
