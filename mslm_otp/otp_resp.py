from dataclasses import dataclass


@dataclass
class OtpResp:
    """
    Data class representing a generic response of an OTP operation.

    Attributes:-
        - code (str): The response code indicating the status of the OTP operation.
        - msg (str): The message associated with the response code.
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


class OtpSendResp(OtpResp):
    """
    Data class representing the response of an OTP sending operation.
    """

    def __str__(self):
        return f"OtpSendResp{{code='{self.code}', message='{self.msg}'}}"


class OtpTokenVerifyResp(OtpResp):
    """
    Data class representing the response of an OTP token verification operation.
    """

    def __str__(self):
        return (
            f"OtpTokenVerifyResp{{code='{self.code}', message='{self.msg}'}}"
        )
