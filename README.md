# Mslm Python SDK

The official Python SDK for the Mslm APIs.

## Installation

```bash
pip install mslm
```

## Usage

```python
from mslm import Mslm
from otp.otp_req import OtpReq

m = Mslm("api_key")

# Email Verify
ev_resp = m.email_verify.single_verify("support@mslm.io")

# Otp
otp_req = OtpReq(
    phone="+923214444444",
    tmpl_sms="Your verification code is {token}",
    token_len=6,
    expire_seconds=300
)

otp_resp = m.otp.send_otp(otp_req)
```

## About Mslm

mslm focuses on producing world-class business solutions. It’s the
bread-and-butter of our business to prioritize quality on everything we touch.
Excellence is a core value that defines our culture from top to bottom.

[![image](https://avatars.githubusercontent.com/u/50307970?s=200&v=4)](https://mslm.io/)
