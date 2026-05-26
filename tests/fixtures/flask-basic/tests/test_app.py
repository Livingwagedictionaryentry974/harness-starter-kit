import unittest

from sample_flask import create_app


class AppTests(unittest.TestCase):
    def test_index(self) -> None:
        client = create_app().test_client()

        response = client.get("/")

        self.assertEqual(b"fixture", response.data)
