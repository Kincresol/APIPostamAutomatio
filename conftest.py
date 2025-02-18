import json
import os
from datetime import datetime

import pytest


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Add timestamp to report file name
    report_dir = "reports"
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    config.option.html_path = f"{report_dir}/Report_{now}.html"


@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    print("\nSetting Up Resources")
    yield
    print("\nTearing Down Resources")


@pytest.fixture
def load_user_data():
    json_file_path = os.path.join(os.path.dirname(__file__), "data", "Testdata.json")
    with open(json_file_path) as json_file:
        data = json.load(json_file)
    return data