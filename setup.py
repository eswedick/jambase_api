from setuptools import setup, find_packages

requirements = ["requests==2.31.0"]
setup_requirements = ["pytest~=7.4.3",
                      "twine==1.14.0"]

test_requirements = ['pytest>=3', ]

setup(
    name='jambase_api',
    packages=find_packages(include=["jambase_api", "jambase_api.*"]),
    include_package_data=True,
    version='1.0.0',
    description='Python API wrapper for Jambase API',
    author='Evan Swedick',
    license='MIT',
    author_email='eswedick@gmail.com',
    url='https://github.com/eswedick/jambase_api',
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    install_requires=requirements,
    setup_requires=setup_requirements,
    python_requires='>=3.9',
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False,
)
