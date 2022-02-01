import requests


def get_contr(*args, **kwargs):
    params_dict = {**kwargs}

    response = requests.get(r'https://api-fns.ru/api/egr', params=params_dict)

    return print(response.json())

print(get_contr(req='280102572282', key='69257345b1cc587c29cb45c9745a65c419a6cfc0'))