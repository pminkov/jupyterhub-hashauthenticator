from setuptools import setup

setup(
    name='jupyterhub-hashauthenticator',
    version='0.1.2',
    description='Hashed Password Authenticator for JupyterHub',
    url='https://github.com/pminkov/jupyterhub-hashauthenticator',
    author='Petko Minkov',
    author_email='pminkov@gmail.com',
    scripts=['hashauthenticator/hashauthenticator'],
    install_requires=['jupyterhub'],
    test_suite="hashauthenticator.tests",
    license='BSD3',
    packages=['hashauthenticator'],
)
