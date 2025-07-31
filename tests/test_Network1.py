#network intercepting with fake payload
#to check in case if there are no products ordered at all - it should display a specific msg
import json
from playwright.sync_api import Playwright, Page, expect
import pytest

fakePayloadOrderResponse = {"data":[],"message":"No Orders"}

def intercept_response(route):
    route.fulfill(
        json = fakePayloadOrderResponse
    )

@pytest.mark.smoke
def test_Network_1(page:Page, user_cred, url_data):
    
    #navigate(web)
    page.goto(url_data["url1"])
    #route to ORDERS with no orders - intercept response method
    page.route(url_data["url2"], intercept_response)
    
    #login(web)
    page.get_by_placeholder("email@example.com").fill(user_cred['user_email'])
    page.get_by_placeholder("enter your passsword").fill(user_cred['user_password'])
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    
    #verify the msg "no products to dsplay"
    #expect(page.locator("body")).to_have_text(" You have No Orders to show at this time.")
    noOrderMsg = page.locator(".mt-4").text_content()
    print(noOrderMsg)