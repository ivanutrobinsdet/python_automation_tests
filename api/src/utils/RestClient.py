import requests


class RestClient:
    API_URL = "https://api.realworld.show/api"
    AUTHORIZATION_HEADER: dict[str, str] = None

    def get_request(self, end_point, params):
        req = requests.get(url=RestClient.API_URL + end_point,
                           params=params,
                           headers=self.AUTHORIZATION_HEADER)
        return req.json()

    def post_request(self, end_point, body=None):
        req = requests.post(url=RestClient.API_URL + end_point,
                            json=body.model_dump(exclude_none=True),
                            headers=self.AUTHORIZATION_HEADER)
        return req

    def put_request(self, end_point, body=None):
        req = requests.put(url=RestClient.API_URL + end_point,
                           json=body.model_dump(exclude_none=True),
                           headers=self.AUTHORIZATION_HEADER)
        return req.json()

    def del_request(self, end_point):
        req = requests.delete(url=RestClient.API_URL + end_point,
                              headers=self.AUTHORIZATION_HEADER)
        return req.json()

    def set_token(self, token):
        self.AUTHORIZATION_HEADER = {"Authorization": f"Token {token}"}
