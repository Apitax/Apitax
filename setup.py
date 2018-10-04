from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='Apitax',
    packages=find_packages(),  # this must be the same as the name above
    version='3.0.0',
    description='Brings together Commandtax, Scriptax, Standard Library, and the API to create a powerful automation framework. Please use StarterPack to quickly incorporate additional drivers, configuration, and custom code into Apitax.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Shawn Clake',
    author_email='shawn.clake@gmail.com',
    url='https://github.com/Apitax/Apitax',
    keywords=['restful', 'api', 'commandtax', 'scriptax'], 
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    install_requires=[
        'connexion == 1.1.15',
        'flask-jwt-extended',
        'flask-cors',
        'apitaxcore==3.0.2',
        'scriptax==0.0.3',
        'commandtax==0.0.5',
        'scriptaxstd==0.0.2'
    ],
)
