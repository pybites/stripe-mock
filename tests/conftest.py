import pytest

from project import create_app


@pytest.fixture
def app():
    return create_app()
