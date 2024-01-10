from setuptools import setup

LONG_DESCRIPTION = """
    # Mslm OTP Python Library
    Where others see norm, we see opportunity. We build world-class solutions to the toughest problems.
    Excellence is a core value that defines our approach from top to bottom.
    Documentation can be found at [https://github.com/mslmio/sdk-python](https://github.com/mslmio/sdk-python).
    """

setup(
    name="mslm-otp",
    version="1.0.0",
    description="Mslm OTP Python Library",
    long_description=LONG_DESCRIPTION,
    url="https://mslm.io",
    author="Mslm",
    author_email="support@mslm.io",
    license="MIT",
    packages=["mslm_otp", "lib"],
    install_requires=["requests", "dataclasses"],
)
