from dataclasses import dataclass


@dataclass
class SingleVerifyRespMx:
    host: str
    pref: int

    def __str__(self):
        return f"SingleVerifyRespMx{{host='{self.host}', pref={self.pref}}}"

    def get_host(self):
        return self.host

    def get_pref(self):
        return self.pref
