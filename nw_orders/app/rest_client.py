import requests


def load_from_api_json(url, parameters, processing_handler):
    if parameters is None:
        response = requests.get(url)
    else:
        response = requests.get(url, parameters)
    json = response.json()
    return_value = processing_handler(json)
    return return_value
