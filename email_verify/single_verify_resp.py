from dataclasses import dataclass
from typing import List

from email_verify.single_verify_resp_mx import SingleVerifyRespMx


@dataclass
class SingleVerifyResp:
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
    mx: List['SingleVerifyRespMx']  # Forward declaration for type hint

    def __str__(self):
        return (
            f"SingleVerifyResp{{email='{self.email}', username='{self.username}', "
            f"domain='{self.domain}', malformed={self.malformed}, "
            f"suggestion='{self.suggestion}', status='{self.status}', "
            f"has_mailbox={self.has_mailbox}, accept_all={self.accept_all}, "
            f"disposable={self.disposable}, free={self.free}, role={self.role}, "
            f"mx={self.mx}}}"
        )
