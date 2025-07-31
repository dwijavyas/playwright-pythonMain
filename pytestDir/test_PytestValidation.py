
import pytest


@pytest.fixture(scope="function")
def preWork():
    print("I set up function instance")


def test_initialCheck(preWork):
    print("this is first test")

def test_secondCheck(preWork):
    print("this is second test")
