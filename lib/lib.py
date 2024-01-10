import json
from urllib.parse import urlparse
from requests import Session


class Lib:
    """
    Generic utility class for handling HTTP requests and responses.

    Attributes:-
        - api_key (str): The API key used for authentication.
        - http (Session): The HTTP session object for making requests.
        - base_url (ParseResult): Parsed URL for the base endpoint of the API.
        - user_agent (str): The user agent string used in HTTP headers.

    Methods:-
        - __init__(self, api_key: Optional[str] = ""): Constructor method.
        - set_http_client(self, http_client): Sets the HTTP client for making requests.
        - set_base_url(self, base_url_str: str): Sets the base URL for API requests.
        - set_user_agent(self, user_agent: str): Sets the user agent for HTTP requests.
        - set_api_key(self, api_key: str): Sets the API key for authentication.
        - get_user_agent(pkg: str): Static method to generate a user agent string.
        - prepare_url(self, url_path, qp, opt): Prepares the URL for making a request.
        - req_and_resp(self, t_url, opt, method='GET', data=None): Makes an HTTP request and returns the response.
    """

    gson = None

    def __init__(self, api_key: str):
        """
        Initializes a Lib object with an optional API key.

        Parameters:-
            - api_key (str): The API key used for authentication.
        """
        self.api_key = api_key
        self.http = Session()
        self.base_url = urlparse("https://mslm.io")
        self.user_agent = self.get_user_agent("mslm")

    def set_http_client(self, http_client):
        """
        Sets the HTTP client for making requests.

        Parameters:-
            - http_client: The HTTP client object.
        """
        self.http = http_client

    def set_base_url(self, base_url_str: str):
        """
        Sets the base URL for API requests.

        Parameters:-
            - base_url_str (str): The base URL for API requests.
        """
        self.base_url = urlparse(base_url_str)

    def set_user_agent(self, user_agent: str):
        """
        Sets the user agent for HTTP requests.

        Parameters:-
            - user_agent (str): The user agent string.
        """
        self.user_agent = user_agent

    def set_api_key(self, api_key: str):
        """
        Sets the API key for authentication.

        Parameters:
            - api_key (str): The API key used for authentication.
        """
        self.api_key = api_key

    @staticmethod
    def get_user_agent(pkg: str):
        """
        Static method to generate a user agent string.

        Parameters:-
            - pkg (str): The package name.

        Returns:
            - str: The generated user agent string.
        """
        return f"{pkg}/python/1.0.0"

    def prepare_url(self, url_path, qp, opt):
        """
        Prepares the URL for making a request.

        Parameters:-
            - url_path: The path of the URL.
            - qp: Query parameters for the URL.
            - opt: Request options.

        Returns:
            - urlparse: The prepared URL for making the request.
        """
        qp["apikey"] = opt.api_key

        t_url = self.base_url._replace(path=url_path)
        http_url_builder = urlparse(t_url.geturl())

        for key, value in qp.items():
            http_url_builder = http_url_builder._replace(
                query=f"{http_url_builder.query}&{key}={value}"
            )

        return urlparse(http_url_builder.geturl())

    def req_and_resp(self, t_url, opt, method="GET", data=None):
        """
        Makes an HTTP request and returns the response.

        Parameters:-
            - t_url: The URL for the HTTP request.
            - opt: Request options.
            - method (str): The HTTP method ('GET' or 'POST').
            - data: Data to be included in the request (for POST requests).

        Returns:
            - str: The response text from the HTTP request.
        """
        headers = {"User-Agent": opt.get_user_agent()}

        if method.upper() == "GET":
            response = self.http.get(t_url.geturl(), headers=headers)
        elif method.upper() == "POST":
            headers["Content-Type"] = "application/json"
            json_data = json.dumps(data) if data else None
            response = self.http.post(
                t_url.geturl(), headers=headers, data=json_data
            )
        else:
            raise ValueError(
                "Invalid HTTP method. Supported methods are GET and POST."
            )

        return response
