import json
from playwright.sync_api import Playwright, Page, expect
import pytest
from pages.login import LoginPage
from utils.apiBaseMain import APIUtils

#convert json to python util
with open('data/credentials.json') as f:
    test_data  = json.load(f)
    user_credentials_list = test_data["user_credentials"]

#parameterize test with multiple data sets
#to use this param user_credentials - we need to call it using fixture
#when user_credentials_list is pulled as param, it will take 1 cred which iss at 0 index and put it into a var
#declaring pytest fixture 'user_credentials' to call it under main test as fixture
#browserInstance is also a fixture declared in coftest that return a page 
@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright, page: Page, user_credentials, browserInstance, url_data):
    
    #take these as arguments in the pom objects
    userName = user_credentials["user_email"]
    password = user_credentials["user_password"]

    #create order(api)
    api_utils = APIUtils()
    orderID = api_utils.createOrder(playwright, user_credentials, url_data)

    #navigate(web)/login(web)
    loginPage = LoginPage(browserInstance)
    loginPage.navigate(url_data)
    dashboardPage = loginPage.login(userName, password)

    #Orders page/View Order(web)
    ordersHistoryPage = dashboardPage.selectOrders()
    orderDetailsPage = ordersHistoryPage.viewOrder(orderID)
    
    #thank you msg
    orderDetailsPage.successfulOrderMessage()