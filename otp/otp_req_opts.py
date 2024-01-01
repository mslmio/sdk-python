from typing import Optional
from dataclasses import dataclass
from lib.req_opts import ReqOpts


@dataclass
class OtpReqOpts:
    """
    Data class representing options for OTP requests.

    Attributes:-
        - req_opts (ReqOpts): Request options for OTP operations.
        - disable_url_encode (Optional[bool]): Flag indicating whether URL encoding should be disabled (optional).

    Usage:
        otp_req_opts = OtpReqOpts(req_opts=req_opts_instance, disable_url_encode=True)
    """

    req_opts: ReqOpts
    disable_url_encode: Optional[bool]

    def __init__(self, req_opts: ReqOpts, disable_url_encode: Optional[bool] = None):
        """
        Initialize an OtpReqOpts object with the specified attributes.

        Parameters:-
            - req_opts (ReqOpts): Request options for OTP operations.
            - disable_url_encode (Optional[bool]): Flag indicating whether URL encoding should be disabled (optional).
        """
        self.req_opts = req_opts
        self.disable_url_encode = disable_url_encode
