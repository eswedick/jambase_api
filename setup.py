# from distutils.core import setup
# setup(
#     name='jambase_API',
#     packages=[
#         "jambase_API",
#         "jambase_API.APISections",
#         "jambase_API.Classes",
#         "jambase_API.Enums",
#         "jambase_API.ParameterTypes",
#     ],
#     version='1.0.5',
#     description='Python API wrapper for Jambase API',
#     author='Evan Swedick',
#     license='MIT',
#     author_email='eswedick@gmail.com',
#     url='https://github.com/eswedick/jambase_api',
#     keywords=['cookiecutter', 'template', 'package', ],
#     python_requires='>=3.6',
# )
from setuptools import setup

setup(
    name="jambase_api",
    version="1.0.2",
    packages=[
        "jambase_API",
        "jambase_API.APISections",
        "jambase_API.Classes",
        "jambase_API.Enums",
        "jambase_API.ParameterTypes",
    ],
    url="https://github.com/eswedick/jambase_api",
    license="MIT",
    author="Evan Swedick",
    author_email="evan@swedick.io",
    description="Python API wrapper for Jambase API",
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    install_requires=("requests", "packaging"),
)
