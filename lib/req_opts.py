from requests import Session
from urllib.parse import urlparse, urlunparse, ParseResult


class ReqOpts:
    def __init__(self, api_key="", http=None, base_url="https://mslm.io", user_agent="mslm"):
        self.api_key = api_key
        self.http = http if http else Session()
        self.base_url = urlparse(base_url)
        self.user_agent = user_agent

    def get_api_key(self):
        return self.api_key

    def get_http_client(self):
        return self.http

    def get_base_url(self):
        return self.base_url

    def get_user_agent(self):
        return self.user_agent

    # Builder class for ReqOpts
    class Builder:
        def __init__(self):
            self.opts = ReqOpts()

        def with_api_key(self, api_key):
            self.opts.api_key = api_key
            return self

        def with_http_client(self, http):
            self.opts.http = http
            return self

        def with_base_url(self, base_url):
            if isinstance(base_url, ParseResult):
                base_url = urlunparse(base_url)
            self.opts.base_url = base_url
            return self

        def with_user_agent(self, user_agent):
            self.opts.user_agent = user_agent
            return self

        def build(self):
            return self.opts
