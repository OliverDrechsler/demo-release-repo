import pytest

from demo import User, validate_user, validate_email


@pytest.fixture()
def user():
    return User(name="Patrick", email="myemail@gmail.com")


def test_valid_user(user):
    result = validate_user(user)
    assert result.is_valid is True


def test_valid_email(user):
    result = validate_email(user)
    assert result.is_valid is True
