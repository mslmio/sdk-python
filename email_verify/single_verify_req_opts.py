from typing import Optional
from dataclasses import dataclass

from lib import ReqOpts


@dataclass
class SingleVerifyReqOpts:
    """
    Data class representing the request options for a single email verification.

    Attributes:-
        - req_opts (ReqOpts): The request options for the email verification.
        - disable_url_encode (Optional[bool]): Optional flag to disable URL encoding of the email address.

    Methods:-
        - __init__(self, req_opts: ReqOpts, disable_url_encode: Optional[bool] = None): Constructor method.
        - Builder: Builder class for constructing instances of SingleVerifyReqOpts.
    """

    req_opts: ReqOpts
    disable_url_encode: Optional[bool]

    def __init__(self, req_opts: ReqOpts, disable_url_encode: Optional[bool] = None):
        """
        Initializes a SingleVerifyReqOpts object with the specified request options and URL encoding flag.

        Parameters:-
            - req_opts (ReqOpts): The request options for the email verification.
            - disable_url_encode (Optional[bool]): Optional flag to disable URL encoding of the email address.
        """
        self.req_opts = req_opts
        self.disable_url_encode = disable_url_encode

    class Builder:
        """
        Builder class for constructing instances of SingleVerifyReqOpts.

        Methods:-
            - with_req_opts(self, req_opts: ReqOpts): Sets the request options.
            - with_disable_url_encode(self, disable_url_encode: bool): Sets the URL encoding flag.
            - build(self): Builds and returns an instance of SingleVerifyReqOpts.
        """

        def __init__(self):
            self.opts = SingleVerifyReqOpts(req_opts=ReqOpts(), disable_url_encode=False)

        def with_req_opts(self, req_opts: ReqOpts):
            """
            Sets the request options for the SingleVerifyReqOpts object.

            Parameters:-
                - req_opts (ReqOpts): The request options for the email verification.

            Returns:
                - Builder: The builder object for method chaining.
            """
            self.opts.req_opts = req_opts
            return self

        def with_disable_url_encode(self, disable_url_encode: bool):
            """
            Sets the URL encoding flag for the SingleVerifyReqOpts object.

            Parameters:-
                - disable_url_encode (bool): Flag indicating whether URL encoding should be disabled.

            Returns:
                - Builder: The builder object for method chaining.
            """
            self.opts.disable_url_encode = disable_url_encode
            return self

        def build(self):
            """
            Builds and returns an instance of SingleVerifyReqOpts.

            Returns:
                - SingleVerifyReqOpts: An instance of SingleVerifyReqOpts with the specified options.
            """
            return self.opts
