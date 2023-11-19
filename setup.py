from distutils.core import setup
setup(
    name='jambase_api',
    packages=[
        "jambase_api",
        "jambase_api.APISections",
        "jambase_api.Classes",
        "jambase_api.Enums",
        "jambase_api.ParameterTypes",
    ],
    version='1.0.7',
    description='Python API wrapper for Jambase API',
    author='Evan Swedick',
    license='MIT',
    author_email='eswedick@gmail.com',
    url='https://github.com/eswedick/jambase_api',
    long_description=open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    python_requires='>=3.6',
)
# from setuptools import setup
#
# setup(
#     name="jambase_api",
#     version="1.0.6",
#     packages=[
#         "jambase_api",
#         "jambase_api.APISections",
#         "jambase_api.Classes",
#         "jambase_api.Enums",
#         "jambase_api.ParameterTypes",
#     ],
#     url="https://github.com/eswedick/jambase_api",
#     license="MIT",
#     author="Evan Swedick",
#     author_email="evan@swedick.io",
#     description="Python API wrapper for Jambase API",
#     long_description=open("README.md", "r").read(),
#     long_description_content_type="text/markdown",
#     install_requires=("requests", "packaging"),
# )
