import unittest
from app import app

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        self.client.testing = True
       
    def test_login(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
    
    def test_register(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
    
    def test_non_existing_route(self):
        response = self.client.get('/nonexistent')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()