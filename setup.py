from distutils.core import setup
setup(
    name='jambase_api',
    packages=[
        "jambase_API",
        "jambase_API.APISections",
        "jambase_API.Classes",
        "jambase_API.Enums",
        "jambase_API.ParameterTypes",
    ],
    version='1.0.0',
    description='Python API wrapper for Jambase API',
    author='Evan Swedick',
    license='MIT',
    author_email='eswedick@gmail.com',
    url='https://github.com/eswedick/jambase_api',
    keywords=['cookiecutter', 'template', 'package', ],
    python_requires='>=3.6',
)
