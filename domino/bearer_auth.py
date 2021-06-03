from requests.auth import AuthBase, HTTPBasicAuth


class BearerAuth(AuthBase):
    """
    Class for authenticating requests by user supplied token.
    """

    def __init__(self, auth_token):
        self.auth_token = auth_token

    @classmethod
    def from_token_file(cls, path_token_to_file):
        with open(path_token_to_file, 'r') as token_file:
            auth_token = token_file.readline().rstrip()
            return cls(auth_token)

    def __call__(self, r):
        """
        Override the default __call__ method for the AuthBase base class

        More more info, see:
        https://docs.python-requests.org/en/master/user/advanced/
        """
        r.headers["Authorization"] = "Bearer " + self.auth_token
        return r


def get_auth_by_type(api_key=None, auth_token=None, domino_token_file=None):
    if auth_token is not None:
        return BearerAuth(auth_token)
    elif domino_token_file is not None:
        return BearerAuth.from_token_file(domino_token_file)
    else:
        return HTTPBasicAuth('', api_key)