# Mslm Python SDK

The official Python SDK for the Mslm APIs.

## Installation

```bash
pip install mslm
```

## Usage

```python
from mslm import Mslm

m = Mslm("api_key")

# Email Verify
ev_resp = m.email_verify.single_verify("support@mslm.io")
print(ev_resp)
# SingleVerifyResp{
#   email='support@mslm.io',
#   username='support', 
#   domain='mslm.io', 
#   malformed=False, 
#   suggestion='', 
#   status='real',
#   has_mailbox=True, 
#   accept_all=False, 
#   disposable=False, 
#   free=True, 
#   role=False, 
#   mx=[
#   {'host': 'ASPMX.L.GOOGLE.COM.', 'pref': 1}, 
#   {'host': 'ALT1.ASPMX.L.GOOGLE.COM.', 'pref': 5}, 
#   ...
#   ]}


# Otp
otp_req = m.otp.otpReq(
    phone="+923214444444",
    tmpl_sms="Your verification code is {token}",
    token_len=6,
    expire_seconds=300
)

otp_resp = m.otp.send(otp_req)
print(otp_resp)  # OtpResp{code='1000', message='Successfully sent SMS.'}
```

## About Mslm

Mslm focuses on producing world-class business solutions. It’s the
bread-and-butter of our business to prioritize quality on everything we touch.
Excellence is a core value that defines our culture from top to bottom.

[![image](https://avatars.githubusercontent.com/u/50307970?s=200&v=4)](https://mslm.io/)
