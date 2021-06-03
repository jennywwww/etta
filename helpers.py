import requests
import os
import pandas as pd

base_url = 'https://exofop.ipac.caltech.edu/tess/'

def call_php_function(func_name, payload, path=None, index_col=None):
    url = create_url(func_name, payload)
    print(f'Fetching data from {url}')
    if payload['output'] == 'pandas':
        if index_col == None:
            return pd.read_csv(url, delimiter='|')
        else:
            return pd.read_csv(url, delimiter='|', index_col=index_col)
    write_to_path(path, url)

def write_to_path(path, url, default_filename=None):
    res = requests.get(url, allow_redirects=True)
    if not path:
        path = '.'
    if not default_filename:
        default_filename = url.rsplit('/', 1)[-1]
    if os.path.isdir(path):
        path = os.path.join(path, default_filename)
    with open(path, 'wb') as f:
        f.write(res.content)

def create_url(func_name, param_dict):
    url = f'{base_url}{func_name}.php?'
    qsPairs = []
    for key, value in param_dict.items():
        if (key, value) == ('output', 'pandas'):
            value = 'pipe'
        if value:
            qsPairs.append(f'{key}={value}')
    url += '&'.join(qsPairs)
    return url