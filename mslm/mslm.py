from email_verify import EmailVerify
from lib import Lib


class Mslm:
    def __init__(self, api_key=None):
        self.email_verify = EmailVerify(api_key)
        self.lib = Lib(api_key)

    def set_http_client(self, http_client):
        # For simplicity, assume http_client is a requests.Session object
        self.lib.set_http_client(http_client)
        self.email_verify.set_http_client(http_client)

    def set_base_url(self, base_url_str):
        self.lib.set_base_url(base_url_str)
        self.email_verify.set_base_url(base_url_str)

    def set_user_agent(self, user_agent):
        self.lib.set_user_agent(user_agent)
        self.email_verify.set_user_agent(user_agent)

    def set_api_key(self, api_key):
        self.lib.set_api_key(api_key)
        self.email_verify.set_api_key(api_key)
