from setuptools import setup

setup(
    name='mslm-email-verify',
    version='1.0.0',
    description='Mslm Email Verify Python Library',
    packages=['mslm_email_verify', 'lib'],
    install_requires=['requests', 'dataclasses'],
    package_dir={"": ".."},
)
