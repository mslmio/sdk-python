from dataclasses import dataclass


@dataclass
class OtpReq:
    phone: str
    tmpl_sms: str
    token_len: int
    expire_seconds: int

    def __init__(self, phone: str, tmpl_sms: str, token_len: int, expire_seconds: int):
        self.phone = phone
        self.tmpl_sms = tmpl_sms
        self.token_len = token_len
        self.expire_seconds = expire_seconds

    # Builder class for OtpReq.
    class Builder:
        def __init__(self):
            self.req = OtpReq(phone="", tmpl_sms="", token_len=0, expire_seconds=0)

        def with_phone(self, phone: str):
            self.req.phone = phone
            return self

        def with_tmpl_sms(self, tmpl_sms: str):
            self.req.tmpl_sms = tmpl_sms
            return self

        def with_token_len(self, token_len: int):
            self.req.token_len = token_len
            return self

        def with_expire_seconds(self, expire_seconds: int):
            self.req.expire_seconds = expire_seconds
            return self

        def build(self):
            return self.req
