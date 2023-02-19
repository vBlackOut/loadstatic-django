import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="loadstatic-django",
    version="1.0.0",
    author="vBlackOut",
    author_email="vlade782@gmail.com",
    description="it's django load static automatical replace url assets",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vBlackOut/loadstatic",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
