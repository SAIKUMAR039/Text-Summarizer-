import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = "0.0.0"

REPO_NAME="Text-Summarizer-"
AUTH_USER_NAME="SAIKUMAR039"
SRC_REPO="textSummarizer"
AUTHOR_EMAIL="saikumarthota2004@gmail.com"

setuptools.setup(
    name=REPO_NAME+SRC_REPO,
    version=__version__,
    author=AUTH_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small package to summarize text",
    long_description=long_description,
    long_description_content_type="text/markdown",
        url="https://github.com/SAIKUMAR039/Text-Summarizer-",
        package_dir={"": "src"},
        packages=setuptools.find_packages(where="src")
    )
