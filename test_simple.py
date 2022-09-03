import pytest


@pytest.fixture()
def choice_user():
    # выбираем клиента
    user_id = 123
    yield user_id
    print("Удаляем пользователя 123")


@pytest.fixture()
def configure_mobile_browser():
    """Устанавливает мобильное соотношение сторон"""
    print("Я Мобильный!")


@pytest.fixture()
def configure_desktop_browser():
    """Устанавливает десктопное соотношение сторон"""
    print("Я Десктопный!")


# Авторизуемся в github.com
# Создаем репозиторий
# Открываем readme.md

def test_first(configure_mobile_browser):
    print(configure_mobile_browser)


def test_second(configure_desktop_browser):
    print(configure_desktop_browser)
    assert 1 == 1


def test_third(choice_user):
    print(choice_user)
    assert choice_user == 123
