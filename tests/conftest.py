import pytest
from selene import browser
from selene.support import webdriver


@pytest.fixture()
def browser_management():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.timeout = 2
    yield
    browser.clear_local_storage()
    browser.quit()