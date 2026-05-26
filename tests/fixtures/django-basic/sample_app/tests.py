from django.test import SimpleTestCase


class SmokeTests(SimpleTestCase):
    def test_truth(self) -> None:
        self.assertTrue(True)
