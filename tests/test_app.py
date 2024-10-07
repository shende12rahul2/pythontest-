import unittest
from app import create_app

class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()
        self.app.testing = True

    def test_home(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome', str(response.data))

    def test_add(self):
        response = self.app.get('/add/5/3')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 8)

    def test_subtract(self):
        response = self.app.get('/subtract/10/4')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 6)

    def test_multiply(self):
        response = self.app.get('/multiply/3/7')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 21)

    def test_divide(self):
        response = self.app.get('/divide/8/2')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['result'], 4.0)

    def test_divide_by_zero(self):
        response = self.app.get('/divide/8/0')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Cannot divide by zero', str(response.data))

    def test_add_invalid(self):
        response = self.app.get('/add/a/2')
        self.assertEqual(response.status_code, 404)

    def test_subtract_invalid(self):
        response = self.app.get('/subtract/10/b')
        self.assertEqual(response.status_code, 404)

    def test_multiply_invalid(self):
        response = self.app.get('/multiply/10/x')
        self.assertEqual(response.status_code, 404)

    def test_divide_invalid(self):
        response = self.app.get('/divide/10/y')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
