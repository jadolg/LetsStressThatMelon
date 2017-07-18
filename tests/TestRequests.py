import unittest
from main import do_get_request, URL


class RequestTesting(unittest.TestCase):
    def test_request(self):
        self.assertEqual(do_get_request(URL), 200)


if __name__ == '__main__':
    unittest.main()
