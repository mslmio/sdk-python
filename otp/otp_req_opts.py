from typing import Optional
from dataclasses import dataclass
from lib.req_opts import ReqOpts


@dataclass
class OtpReqOpts:
    req_opts: ReqOpts
    disable_url_encode: Optional[bool]

    def __init__(self, req_opts: ReqOpts, disable_url_encode: Optional[bool] = None):
        self.req_opts = req_opts
        self.disable_url_encode = disable_url_encode

    # Builder class for OtpReqOpts.
    class Builder:
        def __init__(self):
            self.opts = OtpReqOpts(req_opts=ReqOpts(), disable_url_encode=False)

        def with_req_opts(self, req_opts: ReqOpts):
            self.opts.req_opts = req_opts
            return self

        def with_disable_url_encode(self, disable_url_encode: bool):
            self.opts.disable_url_encode = disable_url_encode
            return self

        def build(self):
            return self.opts
