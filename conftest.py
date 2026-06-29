import pytest
from selenium import webdriver
from selenium.webdriver.edge.options import Options


@pytest.fixture
def browser():
    option = Options()
    option.add_experimental_option("detach", True)
    # driver = webdriver.Edge(options=option)
    driver = webdriver.Chrome()
    yield driver
    driver.quit()
