import requests


def get_contr(*args, **kwargs):
    params_dict = {**kwargs}

    response = requests.get(r'https://api-fns.ru/api/egr', params=params_dict)

    return print(response.json())

print(get_contr(req='', key=''))
