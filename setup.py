import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="scrcpy_stream-pkg-m-c-frank",
    version="0.0.1",
    author="Martin Christoph Frank",
    author_email="martin.frank@hs-augsburg.de",
    description="A small package for easily and continuously capturing screenshots from scrcpy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/m-c-frank/scrcpy_stream/",
    project_urls={
        "Bug Tracker": "https://github.com/m-c-frank/scrcpy_stream/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
