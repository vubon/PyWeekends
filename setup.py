import setuptools


def get_long_description():
    with open("README.md", "r") as readme:
        return readme.read()


def version():
    from PyWeekends.__version__ import __version__
    return __version__


setuptools.setup(
    name="PyWeekends",
    version=version(),
    author="Vubon Roy",
    author_email="vubon.roy@gmail.com",
    description="A simple Python Weekends lib",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/vubon/PyWeekends.git",
    packages=setuptools.find_packages(),
    python_requires='>=3.9',
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
