import requests
import os
import pandas as pd

base_url = 'https://exofop.ipac.caltech.edu/tess/'

def call_php_function(func_name, payload, path=None, index_col=None):
    """Call PHP function with given payload and process result.

    Args:
        func_name (str): Name of PHP function
        payload (dict): key-value pairs of query parameters. MUST contain key `'output'`.
        path (str, optional): Path to save the result file to. 
            Only relevant if result output is csv, pipe or text.

            * If path provided is a file, the result will be written to that file.
            * If path provided is a directory, the file will be saved in the given directory with a default filename.
            * If `path` is `None`, the file will be saved in the current directory with a default filename.

            Defaults to `None`.
        index_col (int, str, sequence of int / str, or False, optional):
            Only relevant if `payload['output'] == 'pandas'`. 
            Column(s) to use as the row labels of the :py:class:`pandas.DataFrame` object, either given 
            as string name or column index. If a sequence of int / str is given, a MultiIndex is used.
            Defaults to None.

    Returns:
        :py:class:`pandas.DataFrame` or `None`: if `output='pandas'`, a :py:class:`pandas.DataFrame`
        object is returned. 
        Else the result is saved to file and the function returns `None`.
    """
    url = create_url(func_name, payload)
    print(f'Fetching data from {url}')
    if payload['output'] == 'pandas':
        if index_col == None:
            return pd.read_csv(url, delimiter='|')
        else:
            return pd.read_csv(url, delimiter='|', index_col=index_col)
    write_to_path(path, url)

def write_to_path(path, url, default_filename=None):
    """Perform a GET request to the given url and write the result to the given path.

    Args:
        path (str): Path to save the result file to. 
            Only relevant if result output is csv, pipe or text.

            * If path provided is a file, the result will be written to that file.
            * If path provided is a directory, the file will be saved in the given directory with a default filename.
            * If `path` is `None`, the file will be saved in the current directory with a default filename.

        url (str): Request URL.
        default_filename (str, optional): Default filename of result, used if path points to a directory. 
            Defaults to None.
    """
    res = requests.get(url, allow_redirects=True)
    if not path:
        path = '.'
    if not default_filename:
        default_filename = url.rsplit('/', 1)[-1]
    if os.path.isdir(path):
        path = os.path.join(path, default_filename)
    with open(path, 'wb') as f:
        f.write(res.content)
        print(f'Result written to {os.path.abspath(path)}')

def create_url(func_name, param_dict):
    """Given a dictionary of query parameters and the PHP function name, form the 
    corresponding URL.

    Args:
        func_name (str): Name of PHP function.
        param_dict (dict): Key-value pairs of query parameters.

    Returns:
        `str`: the created URL.
    """
    url = f'{base_url}{func_name}.php?'
    qsPairs = []
    for key, value in param_dict.items():
        if (key, value) == ('output', 'pandas'):
            value = 'pipe'
        if value:
            qsPairs.append(f'{key}={value}')
    url += '&'.join(qsPairs)
    return url