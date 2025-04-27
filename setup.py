from setuptools import setup, find_packages

setup(
    name="AC_Keyboard_Sounder",  
    version="0.1.0",
    author="joeyycho",
    author_email="joeyycho@icloud.com",
    description="Animal Crossing keyboard sounder for MacOS",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pygame>=2.0.0",
        "pynput>=1.7.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS",
    ],
    python_requires='>=3.8',
    entry_points={
        "console_scripts": [
            "keyboard-sound=main:main"
        ],
    },
)
