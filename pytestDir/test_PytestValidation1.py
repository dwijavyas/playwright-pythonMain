
import pytest


@pytest.fixture(scope="module") #same as scope="class"
def preWork():
    print("I set up module instance")
    return "pass"

@pytest.fixture(scope="function")
def configWork():
    print("setup config")
    yield
    print("teardown config")


def test_initialCheck(preWork, configWork):
    print("this is first test")
    assert preWork == "pass"

@pytest.mark.smoke
def test_secondCheck(preSetUpWork, configWork):
    print("this is second test")

@pytest.mark.skip
def test_negativeCheck(preWork):
    print("this is first test")
    assert preWork == "fail"
