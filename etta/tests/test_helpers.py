"""
Unit tests for helpers module.
"""

from etta.helpers import create_url, write_to_path, call_php_function
from tools import FileCheck
from pandas import DataFrame
import os

def test_create_url():
    payload = {'output': 'pipe', 'sort': 'tid', 'toi': 127}
    url = create_url('download_toi', payload)
    assert url == 'https://exofop.ipac.caltech.edu/tess/download_toi.php?output=pipe&sort=tid&toi=127'

def test_call_php_function_pandas():
    payload = {'output': 'pandas', 'toi': 251}
    res = call_php_function('download_toi', payload)
    assert isinstance(res, DataFrame)
    assert len(res) >= 1

def test_call_php_function_file():
    payload = {'output': 'pipe', 'toi': 251}
    filename = 'test_call_php_function_file.pipe'
    with FileCheck(filename) as file_check:
        res = call_php_function('download_toi', payload, filename)
        assert res is None
        file_check.check_min_length(2)
