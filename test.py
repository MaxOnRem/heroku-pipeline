import unittest
import app as tested_app
import json


class FlaskAppTests(unittest.TestCase):
	
	def setUp(self):
		self.app = tested_app.app.test_client()

	def test_get_hello_endpoint(self):
		r = self.app.get('/')
		self.assertEqual(r._status_code, 200)
		self.assertEqual(r.get_data(), b'Hey there!!! It is the next work using Heroku ;)')

if __name__ == '__main__':
	unittest.main()
