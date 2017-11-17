
from Handlers.RequestHandler import RequestHandler


class JsonifyHandler():
    def __init__(self):
        super(JsonifyHandler, self).__init__()
    def preview_request(self, endpoint_name, method_name, url, query_params):
        """
        called before a request is processed.

        :param string endpoint_name: the name of the endpoint being requested
        :param string method_name: the name of the method being requested
        :param url: the URL that is being requested.
        :param query_params: dict: the parameters to the url that is being queried, e.g. ?key1=val&key2=val2
        """
        pass
    def after_request(self, endpoint_name, method_name, url, response):
        return response.json()
