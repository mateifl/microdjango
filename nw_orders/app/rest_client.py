import requests
import json
from app.logging import LoggerMixin

logger = LoggerMixin()


def load_from_api_json(url, parameters, processing_handler, handler_params=None):
    """Loads a resource using the GET verb."""
    logger.logger.debug("LOAD URL: %s" % url)
    if parameters is None:
        response = requests.get(url)
    else:
        response = requests.get(url, parameters)
    logger.logger.debug("Response: %d %s" % (response.status_code, response.text))
    json = response.json()
    logger.logger.debug(json)
    if handler_params is None:
        return_value = processing_handler(json)
    else:
        return_value = processing_handler(json, handler_params)
    return return_value


def update(url, body):
    """Update a resource using PATCH verb."""
    json_body = json.dumps(body)
    logger.logger.debug("URL: %s" % url)
    logger.logger.debug("payload: %s" % body)
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(url, json_body, headers=headers)
    if response.status_code >= 400:
        logger.logger.error("Response: %d" % response.status_code)
    else:
        logger.logger.debug("Response: %d" % response.status_code)
    return response.status_code
