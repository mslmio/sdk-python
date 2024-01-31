# Mslm Python SDK

The official Python SDK for the Mslm APIs.

## Installation
To install the main library, use the following command:
```bash
pip install mslm
```

## Usage
```python
import mslm

# Initialize the Mslm object with your API key.
mslm_instance = mslm.Mslm("api_key")
```

#### Email Verify
  - Single Verify
  ```python
    single_verify_response, error = mslm_instance.email_verify.single_verify("support@mslm.io")
    # single_verify_response: SingleVerifyResp, error: Error
  ```

#### OTP
  - Sending an OTP.
  ```python
  # Create an OtpSendReq object.
  otp_send_request = mslm_instance.otp.OtpSendReq(
    phone="+923214444444",
    tmpl_sms="Your verification code is {token}",
    token_len=6,
    expire_seconds=300
  )
  
  otp_send_response, error = mslm_instance.otp.send(otp_send_request)
  # otp_send_response: OtpSendResp, error: Error
  ```  
  - Verifying a token.
  ```python
  # Create an OtpTokenVerifyReq object.
  otp_token_verify_request = mslm_instance.otp.OtpTokenVerifyReq(
    phone="+923214444444",
    token="123456",
    consume=True,
  )
  
  otp_token_verify_response, error = mslm_instance.otp.verify(otp_token_verify_request)
  # otp_token_verify_response: OtpTokenVerifyResp, error: Error
```

Each service can be imported individually as well.
#### Email Verify

```python
import mslm_email_verify

# Initialize the EmailVerify object with your API key.
ev = mslm_email_verify.EmailVerify("api_key")
```

#### OTP

```python
import mslm_otp

# Initialize the Otp object with your API key.
o = mslm_otp.Otp("api_key")
```


### Error Handling

We expose the following error types in the SDK:

#### Common Errors
- `MslmError`: The base error type.

#### Quota-Related Errors
- `RequestQuotaExceededError`: The request quota has been exceeded.

These errors can be accessed as follows:

#### Mslm
- `mslm.MslmError`
- `mslm.RequestQuotaExceededError`

#### Email Verify
- `mslm_email_verify.MslmError`
- `mslm_email_verify.RequestQuotaExceededError`

#### OTP
- `mslm_otp.MslmError`
- `mslm_otp.RequestQuotaExceededError`

### Scripts
We provide a few scripts for development purposes.
- `scripts/generate_requirements.sh`: Generates the requirements.txt file.
- `scripts/publish.sh`: Builds and publishes the package to PyPI.
- `scripts/fmt.sh`: Formats the code using black.

## About Mslm
Mslm focuses on producing world-class business solutions. It’s the
bread-and-butter of our business to prioritize quality on everything we touch.
Excellence is a core value that defines our culture from top to bottom.

[![image](https://avatars.githubusercontent.com/u/50307970?s=200&v=4)](https://mslm.io/)
