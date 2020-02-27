import requests
from app.logging import LoggerMixin

logger = LoggerMixin()


def load_from_api_json(url, parameters, processing_handler, handler_params=None):
    logger.logger.debug("URL: %s" % url)
    if parameters is None:
        response = requests.get(url)
    else:
        response = requests.get(url, parameters)
    logger.logger.debug("Response status: %d" % response.status_code)
    json = response.json()
    if handler_params is None:
        return_value = processing_handler(json)
    else:
        return_value = processing_handler(json, handler_params)
    return return_value


def update(url, body):
    """Update a resource using PATCH verb."""
    logger.logger.debug("URL: %s" % url)
    headers = {'content-type': 'application/json'}
    response = requests.patch(url, body, headers=headers)
    logger.logger.debug("Response status: %d" % response.status_code)
    return response.status_code
