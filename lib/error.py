from dataclasses import dataclass


class Error(Exception):
    """Base class for errors."""

    code: int
    message: str

    def __init__(self, code, message):
        """
            Initialize an Error object with the specified attributes.

            Parameters:-
                - code (str): The error code.
                - message (str): The error message.
        """
        self.code = code
        self.message = message

    def __str__(self):
        return f"Error: code: {self.code}, message: {self.message}"


@dataclass
class RequestQuotaExceededError(Error):
    """
        Error raised when the request quota for the API key has been exceeded.
    """

    message = "Request quota for API key has been exceeded."

    def __init__(self):
        """
            Initialize a RequestQuotaExceededError object
        """
        super().__init__(code=429, message=self.message)

