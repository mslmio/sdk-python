from dataclasses import dataclass


@dataclass
class MslmError(Exception):
    """
    Base class for errors.

    Parameters:-
        - code (int): The error code.
        - message (str): The error message.

    """

    code: int
    message: str

    def __str__(self):
        return f"Error: code: {self.code}, message: {self.message}"


@dataclass
class RequestQuotaExceededError(MslmError):
    """
    Error raised when the request quota for the API key has been exceeded.
    """

    code: int = 429
    message: str = "Request quota for API key has been exceeded."
