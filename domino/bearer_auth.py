from requests.auth import AuthBase, HTTPBasicAuth


class DominoAuth(AuthBase):
    """
    Class for authenticating requests by various user supplied credentials.
    """

    def __init__(self, api_key, auth_token, domino_token_file):
        self._api_key = api_key
        self._auth_token = auth_token
        self._domino_token_file = domino_token_file

    @property
    def auth_token(self):
        """
        Return the auth_token as the preferred credential type.

        Can be supplied as a string, or read from a file.
        """
        if self._auth_token is None:
            if self._domino_token_file:
                with open(self._domino_token_file, 'r') as token_file:
                    self._auth_token = token_file.readline().rstrip()
        return self._auth_token

    def __call__(self, r):
        """
        Override the default __call__ method for the AuthBase base class

        More more info, see:
        https://docs.python-requests.org/en/master/user/advanced/
        """
        if self.auth_token:
            r.headers["Authorization"] = "Bearer " + self.auth_token
            return r
        elif self._api_key:
            # Authenticating via API key is a fallback option
            return HTTPBasicAuth('', self._api_key)
        else:
            # This will presumably result in an exception being thrown sometime later
            return None
