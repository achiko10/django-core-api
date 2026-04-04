from django.test import TestCase

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """Test that 1 + 1 always equals 2."""
        self.assertEqual(1 + 1, 2)

    def test_dashboard_access(self):
        """Test that the dashboard login page is accessible."""
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
