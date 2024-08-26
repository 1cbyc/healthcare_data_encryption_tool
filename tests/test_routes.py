# to test the flask routes added
from app.routes import app
import unittest

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_index_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_post(self):
        response = self.client.post('/', data={'data': 'Test data', 'key': '1234567890123456', 'method': 'aes'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Encrypted Data:', response.data)

if __name__ == '__main__':
    unittest.main()
