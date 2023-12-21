import json
from typing import Optional
from urllib.parse import urlparse
from requests import Session

from email_verify.single_verify_resp import SingleVerifyResp


class Lib:
    gson = None  # Assuming you have a Gson-like library in Python

    def __init__(self, api_key: Optional[str] = ""):
        self.api_key = api_key
        self.http = Session()
        self.base_url = urlparse("https://mslm.io")
        self.user_agent = self.get_user_agent("mslm")

    def set_http_client(self, http_client):
        self.http = http_client

    def set_base_url(self, base_url_str: str):
        self.base_url = urlparse(base_url_str)

    def set_user_agent(self, user_agent: str):
        self.user_agent = user_agent

    def set_api_key(self, api_key: str):
        self.api_key = api_key

    @staticmethod
    def get_user_agent(pkg: str):
        return f"{pkg}/python/1.0.0"

    def prepare_url(self, url_path, qp, opt):
        qp["apikey"] = opt.api_key

        t_url = self.base_url._replace(path=url_path)
        http_url_builder = urlparse(t_url.geturl())

        for key, value in qp.items():
            http_url_builder = http_url_builder._replace(query=f"{http_url_builder.query}&{key}={value}")

        return urlparse(http_url_builder.geturl())

    def req_and_resp(self, t_url, opt):
        headers = {"User-Agent": opt.get_user_agent()}
        response = self.http.get(t_url.geturl(), headers=headers)

        json_data = response.text

        # Assuming json_data is a string containing JSON data
        data_dict = json.loads(json_data)

        # Assuming SingleVerifyResp is a class or dictionary containing the structure you expect
        single_verify_resp = SingleVerifyResp(**data_dict)

        # Now, you can use the parsed SingleVerifyResp object
        return single_verify_resp
