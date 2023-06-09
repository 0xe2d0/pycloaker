from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycloaker",
    packages=setuptools.find_packages(),
    version="0.0.1",
    license="MIT",
    description="Cloaking Module For Python",
    author="0xe2d0",
    url="https://github.com/0xe2d0/pycloaker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url="https://github.com/0xe2d0/pyshield/tarball/master",
    keywords=["claoker","python-cloaking","pycloaker","cloaker","cloaking","seo","python cloaking","flask cloaking"],
    install_requires=["requests","re"],
   classifiers=[
        "Development Status :: 1 - Tests",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)