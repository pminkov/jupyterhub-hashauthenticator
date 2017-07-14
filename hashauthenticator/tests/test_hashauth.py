from unittest import TestCase

from hashauthenticator import HashAuthenticator

class TestAuth(TestCase):
  def setUp(self):
    HashAuthenticator.secret_key = "welcome"

  def test_good_and_bad_password(self):
    h = HashAuthenticator()

    data = {}
    data['username'] = 'petko'
    data['password'] = '2d60aa'

    res = h.authenticate(None, data).result()
    self.assertEqual(res, 'petko')

    data['password'] = 'bad_password'
    res = h.authenticate(None, data).result()
    self.assertEqual(res, None)

class TestPasswordLength(TestCase):
  def setUp(self):
    HashAuthenticator.secret_key = "welcome"
    HashAuthenticator.password_length = 8


  def test_different_length(self):
    h = HashAuthenticator()

    data = {}
    data['username'] = 'petko'
    data['password'] = '2d60aad7'

    res = h.authenticate(None, data).result()


    self.assertEqual(len(data['password']), 8)
    self.assertEqual(res, 'petko')

