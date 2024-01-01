from dataclasses import dataclass


@dataclass
class OtpReq:
    """
    Data class representing an OTP request.

    Attributes:-
        - phone (str): Phone number for which the OTP is requested.
        - tmpl_sms (str): Template for the OTP SMS message.
        - token_len (int): Length of the OTP token.
        - expire_seconds (int): Time duration in seconds for which the OTP is valid.

    Usage:
        otp_request = OtpReq(phone="1234567890", tmpl_sms="Your OTP is: {otp}", token_len=6, expire_seconds=300)
    """

    phone: str
    tmpl_sms: str
    token_len: int
    expire_seconds: int

    def __init__(self, phone: str, tmpl_sms: str, token_len: int, expire_seconds: int):
        """
        Initialize an OtpReq object with the specified attributes.

        Parameters:-
            - phone (str): Phone number for which the OTP is requested.
            - tmpl_sms (str): Template for the OTP SMS message.
            - token_len (int): Length of the OTP token.
            - expire_seconds (int): Time duration in seconds for which the OTP is valid.
        """
        self.phone = phone
        self.tmpl_sms = tmpl_sms
        self.token_len = token_len
        self.expire_seconds = expire_seconds
