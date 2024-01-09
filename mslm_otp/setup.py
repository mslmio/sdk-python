from setuptools import setup

setup(
    name='mslm-otp',
    version='1.0.0',
    description='Mslm OTP Python Library',
    packages=['mslm_otp', 'lib'],
    install_requires=['requests', 'dataclasses'],
    package_dir={"": ".."},
)
