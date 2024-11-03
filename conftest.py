import pytest
from utils.driver_setup import initialize_driver

@pytest.fixture(params=["chrome", "firefox"], scope="class")
def setup(request):
    driver = initialize_driver(request.param)
    request.cls.driver = driver
    yield
    driver.quit()
