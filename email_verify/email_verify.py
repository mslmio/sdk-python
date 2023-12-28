import json
from urllib.parse import urlencode

from .single_verify_req_opts import SingleVerifyReqOpts
from lib import Lib
from lib.req_opts import ReqOpts
from .single_verify_resp import SingleVerifyResp


class EmailVerify:
    def __init__(self, api_key=None):
        self.lib = Lib(api_key)

    def set_http_client(self, http_client):
        self.lib.set_http_client(http_client)

    def set_base_url(self, base_url_str):
        self.lib.set_base_url(base_url_str)

    def set_user_agent(self, user_agent):
        self.lib.set_user_agent(user_agent)

    def set_api_key(self, api_key):
        self.lib.set_api_key(api_key)

    def single_verify(self, email):
        opt = SingleVerifyReqOpts.Builder().with_req_opts(
            ReqOpts.Builder()
            .with_api_key(self.lib.api_key)
            .with_base_url(self.lib.base_url)
            .with_http_client(self.lib.http)
            .with_user_agent(self.lib.user_agent)
            .build()
        ).build()

        qp = {"email": email}

        t_url = self.lib.prepare_url("/api/sv/v1", qp, opt.req_opts)
        resp = self.lib.req_and_resp(t_url, opt.req_opts)

        # Assuming SingleVerifyResp is a class or dictionary containing the structure you expect
        return SingleVerifyResp(**json.loads(resp))

    def single_verify_with_opts(self, email, opts=None):
        opt = SingleVerifyReqOpts.Builder().with_req_opts(
            ReqOpts.Builder().build()
        ).build()

        if opts:
            opt = opts

        if opt.disable_url_encode is not None and not opt.disable_url_encode:
            email = urlencode({"email": email})[6:]

        qp = {"email": email}

        t_url = self.lib.prepare_url("/api/sv/v1", qp, opt.req_opts)
        resp = self.lib.req_and_resp(t_url, opt.req_opts)

        # Assuming SingleVerifyResp is a class or dictionary containing the structure you expect
        return SingleVerifyResp(**json.loads(resp))
