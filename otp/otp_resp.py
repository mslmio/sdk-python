from dataclasses import dataclass


@dataclass
class OtpResp:
    """
    Data class representing the response of an OTP operation.

    Attributes:-
        - code (str): The response code indicating the status of the OTP operation.
        - msg (str): The message associated with the response code.

    Usage:
        otp_response = OtpResp(code="1000", msg="OTP successfully sent.")
    """

    code: str
    msg: str

    def __str__(self):
        """
        Return a string representation of the OtpResp object.

        Returns:
            - str: A formatted string representing the OtpResp object.
        """
        return f"OtpResp{{code='{self.code}', message='{self.msg}'}}"
