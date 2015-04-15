from setuptools import setup
import sys, os

version = '0.1'

if sys.version_info < (2, 7):
    install_requires.append('argparse')	

setup(
    name="hello",
    packages=[ "hello" ],
    author = "boonchu",
    author_email = 'bigchoo@gmail.com',
    description = ("hello world demo with setuptools"),
    long_description = open('README.md').read(),
    license = "BSD",
    keywords = 'example of hello world',
    classifiers = [
	"Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    entry_points = {
        "console_scripts": [
            "hello = hello.say:main",
        ]
    }
)
