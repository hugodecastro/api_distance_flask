import json
import logging
import math
import re

import requests
from app.util import utilities
from flask import jsonify

logs = logging.getLogger('app_logs')

class Distance():

    def calculate_distance(p1, p2):
        """
            Applies the Haversine formula and return the distance between two locations
        """
        logs.info('Calculating distance...')

        # approximate radius of earth in km
        R = 6373.0

        # get latitude and longitude
        p1['lat'] = float(p1['lat'])
        p1['long'] = float(p1['long'])
        p2['lat'] = float(p2['lat'])
        p2['long'] = float(p2['long'])

        dlong = math.radians(p2['long'] - p1['long'])
        dlat = math.radians(p2['lat'] - p1['lat'])

        # Haversine formula
        a = math.sin(dlat / 2)**2 + math.cos(p1['lat']) * math.cos(p2['lat']) * math.sin(dlong / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c

    def format_destination(location):
        """
            Return a string in the specific format: word1+word2+word3...+wordN
        """
        if bool(re.search(r"\s", location)):
            # more than one word in location
            return str("".join(map(str,location)).replace(' ', '+'))
        return str(location)

    def get_lat_long(origin, destination):
        """
            Return latitude and longitude of informed locations
        """
        logs.info('Getting latitude and longitude...')
        # convertion locations into json
        origin_json = json.loads(origin.text)
        destination_json = json.loads(destination.text)

        return [
            origin_json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[0],
            origin_json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[1], 
            destination_json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[0], 
            destination_json['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split(' ')[1]
            ]

    def get_destination(dest):
        logs.info('Getting destination...')

        try:
            origin = requests.get('https://geocode-maps.yandex.ru/1.x/?apikey=71f8265c-edd8-40e2-be92-8ad9fb6edc1e&geocode=Moscow+Ring+Road&lang=en_US&format=json')
        
            destination = requests.get('https://geocode-maps.yandex.ru/1.x/?apikey=71f8265c-edd8-40e2-be92-8ad9fb6edc1e&geocode='+Distance.format_destination(dest)+'&lang=en_US&format=json')

            p1_lat, p1_long, p2_lat, p2_long = Distance.get_lat_long(origin,destination)
            
        except Exception as e:
            response = jsonify({"message": "An internal error has occurred. {}".format(e)})
            return response, 500

        # max and min MKAD Range coordinates
        max_coord = max(utilities.mkad_km)
        min_coord = min(utilities.mkad_km)

        # check if givin location is within MKAD range
        if (float(p2_long) > min_coord[1] and float(p2_long) < max_coord[1]) or (float(p2_lat) > min_coord[0] and float(p2_lat) < max_coord[0]):
            logs.info('Input address is within MKAD range.')
            point_two={'lat': 0, 'long': 0}
            return point_two
        else:
            logs.info('Creating coordinates...')
            point_one={'lat': p1_lat, 'long': p1_long}
            point_two={'lat': p2_lat, 'long': p2_long}

        return str(round(Distance.calculate_distance(point_one, point_two), 2)), point_one, point_two
