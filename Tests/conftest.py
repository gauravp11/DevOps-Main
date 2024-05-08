import pytest

@pytest.fixture(scope="function")
def login_url():
    return "http://44.210.180.95:8000/admin/login/?next=/admin/"
