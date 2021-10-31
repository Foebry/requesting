import json


def handleResponse(response, func, args, keys):
    """
        gatekeep function to handle false requests.

        :param response: response object from api call.
        :type response: <http response>
        :param func: callback function
        :type func: function
        :param args: arguments for callback function
        :type args: list
        :param keys: tree structure of response for retrieval of requested data
        :type keys: list or dictionary
    """
    success = response.status_code == 200
    unauthorized = response.status_code == 401
    not_found = response.status_code == 404
    unresponsive = response.status_code == 504

    if success:
            return traverseResponse(response, keys)

    elif unauthorized:
        print(response)
        print("User is not authorized to make this request.")

    elif not_found: return False

    elif unresponsive:
        print("server is not responding")
        #issues.waitTillResponsive(unresponsive)
        #return func(*args)

    else:
        print("something unexpected went wrong.")
        #self.logger.log(msg=f'{response.status_code} - {response}')


def traverseResponse(response, keys):
    """
        function to retrieve requested data

        :param response: response from api request
        :type response: <http response>
        :param keys: tree structure of response for retrieval of requested_data
        :type keys: None, list or dict
    """
    data = response.json()

    if keys is None: return data

    for key in keys:
        if type(data) == dict and key not in data:
            return False
        data = data[key]

    return data
