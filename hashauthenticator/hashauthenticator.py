from jupyterhub.auth import Authenticator
from tornado import gen
from traitlets import Unicode
import hashlib


class HashAuthenticator(Authenticator):
  salt = Unicode(
    default_value=u'salt',
    allow_none=False,
    config=True,
    help="""
    Key used to encrypt usernames to produce passwords.
    """
  )

  PASSWORD_LENGTH = 6

  @gen.coroutine
  def authenticate(self, handler, data):
    password = data['password']
    username = data['username']

    salt_b = bytes(self.salt, 'utf-8')
    username_b = bytes(username, 'utf-8')
    password_digest = hashlib.sha256(salt_b + username_b).hexdigest()
    expected_password = password_digest[:HashAuthenticator.PASSWORD_LENGTH]

    print('Expected password', expected_password)

    if password == expected_password:
      return username

    return None


if __name__ == '__main__':
  HashAuthenticator.salt = 'course_24'
  h = HashAuthenticator()

  data = {}
  data['username'] = 'petko'
  data['password'] = 'hithere'
  res  = h.authenticate(None, data).result()
  assert(res == None)

  data = {}
  data['username'] = 'petko'
  data['password'] = '366f70'
  res  = h.authenticate(None, data).result()
  assert(res == 'petko')



