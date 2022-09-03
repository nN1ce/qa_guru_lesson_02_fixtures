import pytest
from selene.support.shared import browser


@pytest.fixture()
def size_window():
    browser.config.window_width = 754
    browser.config.window_height = 400


# @pytest.fixture(scope="session", autouse=True)
# def open_browser():
#     print("Я, фикстура, вызываюсь перед тестом!")
#     yield
#     print("Я выполняюсь после теста")
