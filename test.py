import unittest
import requests
from main import application
from app.model.distance_model import Distance

class DistanceTest(unittest.TestCase):

    def test_doc(self):
        tester = application.test_client(self)
        res = tester.get('/distance/doc', content_type='html/text')
        self.assertEqual(res.status_code, 200)


    #Test's the yandex api to get the 1st location (MKAD Moscow, Russian Federation)
    def test_origin(self):
        origin = requests.get('https://geocode-maps.yandex.ru/1.x/?apikey=71f8265c-edd8-40e2-be92-8ad9fb6edc1e&geocode=MKAD+Moscow,Russian+Federation&lang=en_US&format=json')
        self.assertTrue(origin.status_code, 200)

    #Test for the destination inside MKAD coordinate
    def test_destination_inside_MKAD(self):
        distance = Distance.get_destination(dest='Ramenki')
        self.assertEqual(len(distance), 2)

    #Test for the destination inside MKAD coordinate
    def test_destination_inside_MKAD(self):
        distance = Distance.get_destination(dest='Rio de Janeiro')
        self.assertEqual(len(distance), 3)


if __name__ == '__main__':
	unittest.main()