from setuptools import setup

version = '0.1'

setup(
    name="hello",
    packages=["hello"],
    entry_points = {
        "console_scripts": [
            "hello = hello.__main__:main",
        ]
    }
)
