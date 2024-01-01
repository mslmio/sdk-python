from typing import Optional
from dataclasses import dataclass
from lib.req_opts import ReqOpts


@dataclass
class OtpReqOpts:
    """
    Data class representing the request options for OTP (One-Time Password).

    Attributes:-
        - req_opts (ReqOpts): The request options for the OTP operation.
        - disable_url_encode (Optional[bool]): Optional flag to disable URL encoding for the OTP request.

    Methods:-
        - __init__(self, req_opts: ReqOpts, disable_url_encode: Optional[bool] = None): Constructor method.
        - Builder: Builder class for constructing instances of OtpReqOpts.
    """

    req_opts: ReqOpts
    disable_url_encode: Optional[bool]

    def __init__(self, req_opts: ReqOpts, disable_url_encode: Optional[bool] = None):
        """
        Initializes an OtpReqOpts object with the specified request options and URL encoding flag.

        Parameters:-
            - req_opts (ReqOpts): The request options for the OTP operation.
            - disable_url_encode (Optional[bool]): Optional flag to disable URL encoding for the OTP request.
        """
        self.req_opts = req_opts
        self.disable_url_encode = disable_url_encode

    class Builder:
        """
        Builder class for constructing instances of OtpReqOpts.

        Methods:-
            - with_req_opts(self, req_opts: ReqOpts) -> Builder: Sets the request options.
            - with_disable_url_encode(self, disable_url_encode: bool) -> Builder: Sets the URL encoding flag.
            - build(self) -> OtpReqOpts: Builds and returns an instance of OtpReqOpts.
        """

        def __init__(self):
            self.opts = OtpReqOpts(req_opts=ReqOpts(), disable_url_encode=False)

        def with_req_opts(self, req_opts: ReqOpts) -> 'OtpReqOpts.Builder':
            """
            Sets the request options for the OtpReqOpts object.

            Parameters:-
                - req_opts (ReqOpts): The request options for the OTP operation.

            Returns:
                - Builder: The builder object for method chaining.
            """
            self.opts.req_opts = req_opts
            return self

        def with_disable_url_encode(self, disable_url_encode: bool) -> 'OtpReqOpts.Builder':
            """
            Sets the URL encoding flag for the OtpReqOpts object.

            Parameters:-
                - disable_url_encode (bool): Flag indicating whether URL encoding should be disabled.

            Returns:
                - Builder: The builder object for method chaining.
            """
            self.opts.disable_url_encode = disable_url_encode
            return self

        def build(self) -> 'OtpReqOpts':
            """
            Builds and returns an instance of OtpReqOpts.

            Returns:
                - OtpReqOpts: An instance of OtpReqOpts with the specified options.
            """
            return self.opts
