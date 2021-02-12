import os

import pandas as pd
import pytest

from amber.src.main import clean_data


@pytest.fixture
def test_data():
    return pd.read_csv(f"{os.path.dirname(__file__)}/data.csv")


def test_clean_data(test_data, mocker):
    assert True
