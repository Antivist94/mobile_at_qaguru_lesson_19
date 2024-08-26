import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.tag("mobile")
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Wikipedia app_Mobile tests examples")
@allure.story("'Explore' screen check ")
def test_explore_screen_wikipedia():
    with step('Skip onboarding screen'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/view_announcement_text'))
        results.should(be.present)


@allure.tag("mobile")
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Wikipedia app_Mobile tests examples")
@allure.story("'Saved' screen check ")
def test_saved_screen_wikipedia():
    with step('Skip onboarding screen'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()

    with step('Press Saved button on bottom menu'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/navigation_bar_item_icon_view")).element(1).click()

    with step('Verify content found'):
        results = browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))
        results.should(be.present)
        results.first.should(have.text('Saved'))


@allure.tag("mobile")
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Wikipedia app_Mobile tests examples")
@allure.story("'Search' screen check ")
def test_search_screen_wikipedia():
    with step('Skip onboarding screen'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()

    with step('Press Search button on bottom menu'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/navigation_bar_item_icon_view")).element(2).click()

    with step('Verify content found'):
        results = browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))
        results.should(be.present)
        results.first.should(have.text('Search'))


@allure.tag("mobile")
@allure.label("owner", "Evdokimenko Eugene")
@allure.feature("Wikipedia app_Mobile tests examples")
@allure.story("'Edits' screen check ")
def test_edits_screen_wikipedia():
    with step('Skip onboarding screen'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()

    with step('Press Edits button on bottom menu'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/navigation_bar_item_icon_view")).element(3).click()

    with step('Verify content found'):
        results = browser.all((AppiumBy.CLASS_NAME, 'android.widget.TextView'))
        results.should(be.present)
        results.first.should(have.text('Edits'))
