from setuptools import setup

from mslm_email_verify.version import SDK_VERSION

LONG_DESCRIPTION = """
# Mslm Email Verify Python Library

Where others see norm, we see opportunity. We build world-class solutions to the toughest problems. 
Excellence is a core value that defines our approach from top to bottom.
Documentation can be found at [https://github.com/mslmio/sdk-python](https://github.com/mslmio/sdk-python).
"""


setup(
    name="mslm_email_verify",
    version=SDK_VERSION,
    description="Mslm Email Verify Python Library",
    long_description=LONG_DESCRIPTION,
    url="https://mslm.io",
    author="Mslm",
    author_email="support@mslm.io",
    license="MIT",
    packages=["mslm_email_verify", "mslm_lib"],
    install_requires=["requests", "dataclasses"],
)
