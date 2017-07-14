from jupyterhub.auth import Authenticator
from tornado import gen
from traitlets import Unicode, Integer
import hashlib, binascii

def generate_password_digest(username, secret_key):
  dk = hashlib.pbkdf2_hmac('sha256', username.encode(), secret_key.encode(), 25000)
  password_digest = binascii.hexlify(dk).decode()

  return password_digest


class HashAuthenticator(Authenticator):
  secret_key = Unicode(
    config=True,
    help="Key used to encrypt usernames to produce passwords."
  )

  password_length = Integer(
    default_value=6,
    config=True,
    help="Password length.")

  @gen.coroutine
  def authenticate(self, handler, data):
    username = data['username']
    password = data['password']

    password_digest = generate_password_digest(username, self.secret_key)
    expected_password = password_digest[:self.password_length]

    if password == expected_password:
      return username

    return None
