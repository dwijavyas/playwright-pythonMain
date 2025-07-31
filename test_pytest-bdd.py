from pytest_bdd import scenarios, given, when, then, parsers

from playwrightDir.utils.apiBase import APIUtils

# Link the feature file (relative path)
scenarios('../../features/order_transactions.feature')

# Given step: place the item order with username and password
@given(parsers.cfparse('place the item order with {username} and {password}'))
def place_item_order(playwright, user_credentials, username, password):
    user_email = user_credentials["user_email"]
    user_password = user_credentials["user_password"]

    api_utils = APIUtils()
    orderID = api_utils.createOrder(playwright, user_credentials)

# And step: user is on landing page
@given('the user is on landing page')
def user_on_landing_page():
    # Code to verify user is on landing page or navigate there
    print("User on landing page")

# When step: login to portal with username and password
@when(parsers.cfparse('I login to portal with {username} and {password}'))
def login_portal(username, password):
    # Code to perform login
    print(f"Logging in with user: {username}")

# When step: navigate to Orders page
@when('navigate to Orders page')
def navigate_orders_page():
    # Code to navigate to orders page
    print("Navigated to Orders page")

# When step: select the OrderID
@when('select the OrderID')
def select_order_id():
    # Code to select the order ID (maybe last order or specific)
    print("Selected the Order ID")

# Then step: verify the order message
@then('verify the order message')
def verify_order_message

