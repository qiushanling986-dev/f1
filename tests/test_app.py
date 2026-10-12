import unittest
from app import app
class AppTests(unittest.TestCase):
    def test_dashboard_and_assets(self):
        client = app.test_client()
        for path, content in [('/', b'F1 Live Hub'), ('/app.js', b'api.jolpi.ca'), ('/style.css', b'@media')]:
            response = client.get(path)
            self.assertEqual(response.status_code, 200)
            self.assertIn(content, response.data)
    def test_unknown_file(self):
        self.assertEqual(app.test_client().get('/missing').status_code, 404)
    def test_path_traversal(self):
        self.assertEqual(app.test_client().get('/../app.py').status_code, 404)
