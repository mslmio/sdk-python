from dataclasses import dataclass


@dataclass
class OtpSendReq:
    """
    Data class representing an OTP send request.

    Attributes:-
        - phone (str): Phone number for which the OTP is requested.
        - tmpl_sms (str): Template for the OTP SMS message.
        - token_len (int): Length of the OTP token.
        - expire_seconds (int): Time duration in seconds for which the OTP is valid.

    Usage:
        otp_request = OtpSendReq(phone="1234567890", tmpl_sms="Your OTP is: {mslm_otp}", token_len=6, expire_seconds=300)
    """

    phone: str
    tmpl_sms: str
    token_len: int
    expire_seconds: int
