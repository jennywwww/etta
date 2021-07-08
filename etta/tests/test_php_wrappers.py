"""
Unit tests for php_wrappers module.

Running tests which are NOT marked as slow (default):
    python -m pytest test_php_wrappers.py
These tests take about 30 seconds to run (on my local machine).

Running all tests, including those marked as slow:
    python -m pytest test_php_wrappers.py --runslow
These tests take a VERY long time, upwards of 30 minutes (on my local machine).
"""

from etta.php_wrappers import *
from tools import FileCheck
from pandas import DataFrame
import os
import pytest

def wrapper_tester(func, params, expected_rows, expected_cols):
    res = func(**params)
    assert len(res) >= expected_rows
    assert len(res.columns) >= expected_cols

    filename = f'test_{func.__name__}.csv'
    with FileCheck(filename) as file_check:
        res = func(**params, output='csv', path=filename)
        assert res is None
        file_check.check_min_length(expected_rows + 1)

def test_download_toi_single():
    wrapper_tester(
        download_toi,
        {'toi': 174},
        expected_rows=4,
        expected_cols=57
    )

@pytest.mark.slow
def test_download_toi_all():
    res = download_toi(sort='sg1a')
    assert res['SG1A'].is_monotonic
    assert len(res) >= 4198
    assert len(res.columns) >= 57

def test_download_nearbytarget():
    wrapper_tester(
        download_nearbytarget,
        {'tic': 278683844, 'sort': 'tmag'},
        expected_rows=12,
        expected_cols=14
    )

def test_download_imaging_single():
    wrapper_tester(
        download_imaging,
        {'target': 26474039},
        expected_rows=8,
        expected_cols=15
    )

@pytest.mark.slow
def test_download_imaging_all():
    res = download_imaging(sort='user')
    assert res['User'].is_monotonic
    assert len(res) >= 16382
    assert len(res.columns) >= 15

def test_download_tag_imaging():
    wrapper_tester(
        download_tag_imaging,
        {'tag': 95132},
        expected_rows=2,
        expected_cols=15
    )

def test_download_spect_single():
    wrapper_tester(
        download_spect,
        {'target': 'TOI1162'},
        expected_rows=4,
        expected_cols=15
    )

@pytest.mark.slow
def test_download_spect_all():
    res = download_spect(sort='inst')
    assert res['Instrument'].is_monotonic
    assert len(res) >= 14802
    assert len(res.columns) >= 15

def test_download_tag_spect():
    wrapper_tester(
        download_tag_spect,
        {'tag': 1494},
        expected_rows=9,
        expected_cols=15
    )

def test_download_tseries_single():
    wrapper_tester(
        download_tseries,
        {'target': 366074069},
        expected_rows=6,
        expected_cols=19
    )

@pytest.mark.slow
def test_download_tseries_all():
    res = download_tseries(sort='user')
    assert res['User'].is_monotonic
    assert len(res) >= 6373
    assert len(res.columns) >= 19

def test_download_tag_tseries():
    wrapper_tester(
        download_tag_tseries,
        {'tag': 7},
        expected_rows=2,
        expected_cols=19
    )

def test_download_obsnotes():
    wrapper_tester(
        download_obsnotes,
        {'tag': 3059},
        expected_rows=1185,
        expected_cols=7
    )

    wrapper_tester(
        download_obsnotes,
        {'tic': 254113311},
        expected_rows=3,
        expected_cols=7
    )

    wrapper_tester(
        download_obsnotes,
        {'row_id': 4339},
        expected_rows=1,
        expected_cols=7
    )

@pytest.mark.slow
def test_download_user_tags():
    """This test is extremely slow (can take about 30 minutes).
    """
    wrapper_tester(
        download_user_tags,
        {'username': 'ciardi'},
        expected_rows=19043,
        expected_cols=13
    )

def test_download_stellarcomp_single():
    wrapper_tester(
        download_stellarcomp,
        {'target': 27769688},
        expected_rows=3,
        expected_cols=15
    )

def test_download_stellarcomp_all():
    res = download_stellarcomp(sort='id')
    assert res['TIC ID'].is_monotonic
    assert len(res) >= 4017
    assert len(res.columns) >= 15
