from setuptools import setup

setup(
    name='jupyterhub-hashauthenticator',
    version='0.1',
    description='Hashed Password Authenticator for JupyterHub',
    url='https://github.com/pminkov/jupyterhub-hashauthenticator',
    author='Petko Minkov',
    author_email='pminkov@gmail.com',
    scripts=['hashauthenticator/hashauthenticator'],
    test_suite="hashauthenticator.tests",
    license='MIT',
    packages=['hashauthenticator'],
)
