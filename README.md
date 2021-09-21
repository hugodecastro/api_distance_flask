## Description:

Develop a Flask Blueprint to find the distance from the [Moscow Ring Road](https://en.wikipedia.org/wiki/Moscow_Ring_Road) to the specified address. The address is passed to the application in an HTTP request, if the specified address is located inside the MKAD, the distance does not need to be calculated. Add the result to the .log file.

To calculate the distance between points, we suggest using the [**Yandex Geocoder API**](https://yandex.ru/dev/maps/geocoder/doc/desc/concepts/about.html) 
The developer key can be obtained for free upon registration.

## Tools
- Python 3.8
- Yandex Geocoder API
- Docker
- Google Maps API

## Setup
### Localhost
- git clone
- pip install -r requirements.txt
- run python main.py
- Press http://127.0.0.1:5000 to see documentation page

### Docker
- docker build -t distance_calculator -f Dockerfile .
- docker run distance_calculator

## Optional Setup

It is necessary to genete a API Key on [Google Maps Platform](https://cloud.google.com/maps-platform/) so the code can run propely as seen below:
![Example](https://github.com/hugodecastro/api_distance_flask/tree/main/app/util/img/example.PNG?raw=true)

## Authors
- [@hugodecastro](https://github.com/hugodecastro)
