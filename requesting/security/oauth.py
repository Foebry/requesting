import requests

from requesting import issues
from requesting.responses import handleResponse


def getAccessToken(endpoint, data, request_data):
    """
        function to retrieve the access_token for oauth security level api.

        :param endpoint: endpoint to send request to
        :type endpoint: string
        :param data: data to send with request
        :type data: dictionary
        :param request_data: tree structure for data to retrieve
        :type request_data: list, dictionary or None

        return "USpQNKdGSbJCTmv5A1Niz6HxDxRBQQPvh0"
    """

    try: response = requests.post(endpoint, data=data)
    except requests.exceptions.ConnectionError:
        return issues.reconnect(getAccessToken, (data, request_data))

    return handleResponse(response, getAccessToken, (data, request_data), request_data)


def get(endpoint, request_data):
    """
        API get requests for oauth authentication

        :param endpoint: endpoint to send request to
        :type endpoint: string
    """

    try: response = requests.get(endpoint, request_data)
    except requests.exceptions.ConnectionError:
        return issues.reconnect(get, (endpoint, request_data))

    return handleResponse(response, get, (endpoint, request_data), request_data)
