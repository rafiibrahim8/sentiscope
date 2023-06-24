import unittest

from app import app

class TestResponse(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.app = app
        cls.app.config['TESTING'] = True
        cls.client = app.test_client()

    def test_analyze(self):
        response = self.client.post('/api/v1/analyze', json={'text': 'I love this project!'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json.get('sentiment'), 'positive')

    def test_analyze_invalid_payload(self):
        response = self.client.post('/api/v1/analyze', json='I love you')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid payload'})

    def test_analyze_missing_text(self):
        response = self.client.post('/api/v1/analyze', json={'foo': 'bar'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid payload'})
