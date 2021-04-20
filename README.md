# Hash JupyterHub Authenticator

An authenticator for [JupyterHub](https://jupyterhub.readthedocs.io/en/latest/) where the password for each user is a secure hash of its username. Useful for environments where it's not suitable for users to authenticate with their Google/GitHub/etc. accounts.

## Installation

```bash
pip install jupyterhub-hashauthenticator
```

Should install it. It has no additional dependencies beyond JupyterHub.

You can then use this as your authenticator by adding the following line to your jupyterhub_config.py:

```python
c.JupyterHub.authenticator_class = 'hashauthenticator.HashAuthenticator
c.HashAuthenticator.secret_key = 'my secret key'
```

You can generate a good secret key with:
```bash
$ openssl rand -hex 32
0fafb0682a493485ed4e764d92abab1199d73246477c5daac7e0371ba541dd66
```

## Generating the password

This package comes with a command called `hashauthenticator`. Example usage:

```bash
$ hashauthenticator
Usage: hashauthenticator secret_key user [len]

$ hashauthenticator my_key pminkov
939fd4
```
