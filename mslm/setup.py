from setuptools import setup

setup(
    name='mslm',
    version='1.0.0',
    description='Mslm Python Library',
    packages=['mslm', 'lib', 'mslm_email_verify', 'mslm_otp'],
    install_requires=['requests', 'dataclasses'],
    package_dir={"": ".."},
)
