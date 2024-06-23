import unittest
from unittest.mock import patch
from src.website_reader import WebsiteReader

class TestWebsiteReader(unittest.TestCase):

    @patch('requests.get')
    def test_fetch_content_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.text = "Mocked content"

        reader = WebsiteReader("https://www.example.com")
        result = reader.fetch_content()

        self.assertEqual(result, "Mocked content")

    @patch('requests.get')
    def test_fetch_content_failure(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404

        reader = WebsiteReader("https://www.example.com")
        result = reader.fetch_content()

        self.assertIn("Failed to fetch content", result)

    @patch('requests.get')
    def test_fetch_content_exception(self, mock_get):
        mock_get.side_effect = Exception("Mocked exception")

        reader = WebsiteReader("https://www.example.com")
        result = reader.fetch_content()

        self.assertIn("Error fetching content", result)

if __name__ == "__main__":
    unittest.main()
