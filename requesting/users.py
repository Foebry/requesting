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
            data = {data["client_id"], data["client_secret"]}
            self.access_token = oauth.getAccessToken(endpoint, data, request_data)
            self.security = data["security"]


    def get(self, endpoint, request_data=None):
        """
            get api calls

            :param endpoint:
        """
        if self.security == "oauth": return oauth.get(endpoint, request_data)

if __name__ == "__main__":
    user = User("")

    user.authenticate({'security':'oauth','grant_type':'client_credentials',
                    'client_id': "2d145be238fc4068a18cd9a2cb7473eb",
                    'client_secret': "m6eqhka7BWQxVJc9dYn2cO70zLYHE2uo"}, "https://us.battle.net/oauth/token", ("access_token",))

    print(user.access_token)
