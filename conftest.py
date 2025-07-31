import json
import pytest

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="my option: select browser"
    )

@pytest.fixture(scope="session")
def preSetUpWork():
    print("I set up session instance")

#fixture user_credentials is called in test_web_api which is placed here
#under that fixture we are returning user_cred param is requesting if theres any parameter for the fixture user_credentials - under pytest.mark.parameterize 
@pytest.fixture(scope="session")
def user_credentials(request):
    return request.param

@pytest.fixture(scope="session")
def user_cred():
    with open('data/credentials.json') as f:
        test_dataN1N2 = json.load(f)
        return test_dataN1N2['user_credentials'][0]
    
@pytest.fixture(scope="session")
def url_data():
    with open('data/urls.json') as f:
        test_url = json.load(f)
        return test_url['urls_list']

@pytest.fixture()
def browserInstance(playwright, request):

    #request to get parameter like browser config from terminal
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        browser = playwright.chromium.launch(headless=False, args=["--disable-features=AudioServiceOutOfProcess"])
    elif browser_name == "firefox":
        browser = playwright.firefox.launch(headless=False)

    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()
    browser.close()
   
