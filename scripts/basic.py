import requests

endpoint = 'http://127.0.0.1:8000/api/?m=10'


def run():
    get_response = requests.get(endpoint)
    print(get_response.json())
    # print(get_response.json()['message'])
    # print(get_response.status_code)
