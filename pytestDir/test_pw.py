#playwright and page are in built fixtures provided by pw
#page fixture to only use with chromium with headless mode (chrome and edge) not with firefox and headed

import time
from playwright.sync_api import Playwright, Page, expect


def test_pwBasics(playwright: Playwright):
    browser= playwright.chromium.launch(headless=False)
    context = browser.new_context() #isolated/fresh window
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")
    #yield
    #browser.close()

def test_pwShortCut(page: Page):
    page.goto("https://rahulshettyacademy.com")

def test_coreLocators(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    #restrictions
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learningfgfg")
    #css
    page.locator('#terms').check()
    #restrictions
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link", name="terms and condition").click()
    page.get_by_role("button", name="Sign In").click()
    #error
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

    time.sleep(5)


def test_pwFirefox(playwright: Playwright):
    firefoxbrowser=playwright.firefox
    browser = firefoxbrowser.launch(headless=False)
    page = browser.new_page()
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    #restrictions
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learningfgfg")
    #css
    page.locator('#terms').check()
    #restrictions
    page.get_by_role("combobox").select_option("teach")
    page.get_by_role("link", name="terms and condition").click()
    page.get_by_role("button", name="Sign In").click()
    #error
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()

    time.sleep(5)