from dataclasses import dataclass
from typing import List

from .single_verify_resp_mx import SingleVerifyRespMx


@dataclass
class SingleVerifyResp:
    """
    Data class representing the response of a single email verification.

    Attributes:-
        - email (str): The email address being verified.
        - username (str): The username part of the email address.
        - domain (str): The domain part of the email address.
        - malformed (bool): Indicates whether the email address is malformed.
        - suggestion (str): A suggested correction for the email address if it is malformed.
        - status (str): The status of the email verification (e.g., "valid" or "invalid").
        - has_mailbox (bool): Indicates whether the email address has a mailbox.
        - accept_all (bool): Indicates whether the email domain accepts all emails.
        - disposable (bool): Indicates whether the email address is disposable.
        - free (bool): Indicates whether the email address is from a free email provider.
        - role (bool): Indicates whether the email address represents a role (e.g., admin@domain.com).
        - mx (List[SingleVerifyRespMx]): List of mail exchange (MX) records associated with the email domain.
    """

    email: str
    username: str
    domain: str
    malformed: bool
    suggestion: str
    status: str
    has_mailbox: bool
    accept_all: bool
    disposable: bool
    free: bool
    role: bool
    mx: List["SingleVerifyRespMx"]  # Forward declaration for type hint

    def __str__(self):
        """
        Returns a string representation of the SingleVerifyResp object.

        Returns:
            - str: A string representation of the SingleVerifyResp object.
        """
        return (
            f"SingleVerifyResp{{email='{self.email}', username='{self.username}', "
            f"domain='{self.domain}', malformed={self.malformed}, "
            f"suggestion='{self.suggestion}', status='{self.status}', "
            f"has_mailbox={self.has_mailbox}, accept_all={self.accept_all}, "
            f"disposable={self.disposable}, free={self.free}, role={self.role}, "
            f"mx={self.mx}}}"
        )
