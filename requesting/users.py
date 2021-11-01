import requests

from requesting.security import oauth



class User:
    """
        User is the overarching entity of a request platform.
    """

    def __init__(self, endpoint):
        """
            Create a user entity.

            :param endpoint: endpoint for the api requests.
            :type endpoint: string
        """
        if type(endpoint) != str: raise TypeError("endpoint has to be a string.")
        self.endpoint = endpoint
        self.access_token = None
        self.security = None


    def authenticate(self, data, endpoint, request_data=None):
        if data['security'] == "oauth":
            self.access_token = oauth.getAccessToken(endpoint, data["CREDENTIALS"], request_data)
            self.security = data["security"]


    def get(self, endpoint, request_data=None):
        """
            get api calls

            :param endpoint:
        """
        if self.security == "oauth": return oauth.get(endpoint, request_data)
