import json

from lib import Lib
from lib.req_opts import ReqOpts
from otp.otp_req import OtpReq
from otp.otp_req_opts import OtpReqOpts
from otp.otp_resp import OtpResp


class Otp:
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

    def send_otp(self, otp_req: OtpReq):
        opt = OtpReqOpts.Builder().with_req_opts(
            ReqOpts.Builder()
            .with_api_key(self.lib.api_key)
            .with_base_url(self.lib.base_url)
            .with_http_client(self.lib.http)
            .with_user_agent(self.lib.user_agent)
            .build()
        ).build()

        qp = {
            "phone": otp_req.phone,
            "tmpl_sms": otp_req.tmpl_sms,
            "token_len": otp_req.token_len,
            "expire_seconds": otp_req.expire_seconds
        }

        t_url = self.lib.prepare_url("/api/otp/v1/send", qp, opt.req_opts)
        resp = self.lib.req_and_resp(t_url, opt.req_opts, method='POST')

        return OtpResp(**json.loads(resp))

    def send_otp_with_opts(self, otp_req: OtpReq, opts=None):
        opt = OtpReqOpts.Builder().with_req_opts(
            ReqOpts.Builder().build()
        ).build()

        if opts:
            opt = opts

        qp = {
            "phone": otp_req.phone,
            "tmpl_sms": otp_req.tmpl_sms,
            "token_len": otp_req.token_len,
            "expire_seconds": otp_req.expire_seconds
        }

        t_url = self.lib.prepare_url("/api/otp/v1/send", qp, opt.req_opts)
        resp = self.lib.req_and_resp(t_url, opt.req_opts, method='POST')

        return OtpResp(**json.loads(resp))
