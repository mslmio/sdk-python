from dataclasses import dataclass


@dataclass
class OtpTokenVerifyReq:
    """
    Data class representing an OTP token verification request.

    Attributes:-
        - phone (str): The phone number associated with the OTP token.
        - token (str): The OTP token to be verified.
        - consume (bool): A flag indicating whether to consume the OTP token after verification.

    Usage:
        request = OtpTokenVerifyReq(phone="1234567890", token="123456", consume=True)
    """

    phone: str
    token: str
    consume: bool
