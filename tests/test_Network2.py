#order history of another user should not be displayed if logged in using another account
#verify the 'no authorization' msg if thats the case
import json
import time
from playwright.sync_api import Playwright, Page, expect
import pytest
from utils.apiBaseMain import APIUtils

def intercept_request(route, request, url_data):
    route.continue_(url=url_data["url4"])

def test_Network_2(playwright: Playwright, page: Page, user_cred, url_data):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #navigate(web)
    page.goto(url_data["url1"])
    #route to ORDERS with no orders - intercept response method
    page.route(url_data["url3"], 
               lambda route, request: intercept_request(route, request, url_data))
    #login(web)
    page.get_by_placeholder("email@example.com").fill(user_cred["user_email"])
    page.get_by_placeholder("enter your passsword").fill(user_cred["user_password"])
    page.get_by_role("button", name="Login").click()

    #Orders page/View Order(web)
    page.get_by_role("button", name="ORDERS").click()

    #click on view the order and thats when "unauthorized msg"
    page.get_by_role("button", name="VIEW").first.click()
    noAuth = page.locator(".blink_me").text_content()
    print(noAuth)

#this is for extracting the token from api to avoid signing in everytime
def test_session_storage(playwright: Playwright, user_cred, url_data):
    api_utils = APIUtils()
    token = api_utils.getToken(playwright, user_cred, url_data)
    
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #inject token form ispect element/application/local storage
    page.add_init_script(f"""localStorage.setItem('token', '{token}')""")

    #navigate(web)
    page.goto(url_data["url1"])

    #Orders page/View Order(web)
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text("Your Orders")).to_be_visible()




