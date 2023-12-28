from dataclasses import dataclass


@dataclass
class OtpResp:
    code: str
    msg: str

    def __str__(self):
        return f"OtpsResp{{code='{self.code}', message='{self.msg}'}}"
