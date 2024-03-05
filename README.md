# Mslm Python SDK

The official Python SDK for Mslm APIs.

## Requirements

Before you start using the Mslm Python SDK, ensure that you have the following:

- **Python:** The SDK is compatible with Python 3.6 and above.

## Authentication

Mslm's APIs require an API key. If you don't have one, please read
[Authentication](https://mslm.io/docs/api/authentication) to understand how to
get an API key before continuing.

## Installation
To install the main library, use the following command:

```bash
pip install mslm
```

Or install specific packages like `mslm-email-verify` and `mslm-otp` separately:

```bash
pip install mslm-email-verify
pip install mslm-otp
```

## Usage

```python
import mslm

# Initialize the Mslm object with your API key.
client = mslm.Mslm("api_key")
```

#### Email Verify
  - Single Verify
  ```python
    resp, error = client.email_verify.single_verify("support@mslm.io")
  ```

#### OTP
  - Sending an OTP.
  ```python
  # Create an OtpSendReq object.
  otp_send_request = client.otp.OtpSendReq(
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
mslm_email_verify_instance = mslm_email_verify.EmailVerify("api_key")
```

#### OTP

```python
import mslm_otp

# Initialize the Otp object with your API key.
mslm_otp_instance = mslm_otp.Otp("api_key")
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
- `scripts/publish.sh`: Builds and publishes the package to PyPI.
- `scripts/fmt.sh`: Formats the code using black.

## Additional Resources

See the official [API Reference Documentation](https://mslm.io/docs/api) for
details on each API's actual interface, which is implemented by this SDK.

## Contributing

See [CONTRIBUTING](CONTRIBUTING.md) for more information.

## Security

See [Security Issue
Notifications](CONTRIBUTING.md#security-issue-notifications) for more
information.

## License

This project is licensed under the [MIT License](LICENSE).

## About Mslm

At Mslm, we're all about making things better. Where others see norm, we see
opportunity.

We build world-class solutions to the toughest problems. Excellence is a core
value that defines our approach from top to bottom.

We're all about creating positive value for ourselves, our partners and our
societies.

We do it by focusing on quality and the long-term, while intelligently
maneuvering the complex realities of day-to-day business.

Our partners share our perspective, and we jointly produce truly world-class
solutions to the toughest problems.

[![image](https://avatars.githubusercontent.com/u/50307970?s=200&v=4)](https://mslm.io/)
