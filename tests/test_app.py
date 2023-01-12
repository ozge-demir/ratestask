import unittest
from src import app


class TestAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_average_prices(self):
        # Test with valid input
        response = self.app.get(
            '/rates?date_from=2016-01-01&date_to=2016-01-10&origin=CNSGH&destination=north_europe_main')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json,
                         [{'day': '2016-01-01', 'average_price': 1112}, {'day': '2016-01-02', 'average_price': 1112},
                          {'day': '2016-01-03', 'average_price': None}, ...])

        # Test with invalid input
        response = self.app.get('/rates?date_from=2016-01-01&date_to=2016-01-10&origin=invalid&destination=invalid')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {'error': 'Invalid origin or destination'})

        # Test with missing parameters
        response = self.app.get('/rates?date_from=2016-01-01&destination=north_europe_main')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.content_type, 'application/json')
        self.assertEqual(response.json, {'error': 'Missing date_to or origin parameter'})

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
