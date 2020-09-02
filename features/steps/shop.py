from behave import *
from pages.page_objects import GuestShopper

use_step_matcher("re")
driver  = GuestShopper()


@given('I am on "jumia" website')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.set_up()


@step("I search for an item")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.search_item()


@step("I click on search button")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.click_search_button()


@step("I select an item")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.select_item()


@step("I added the item to cart")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.add_to_cart()


@step("I click on view cart and checkout")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.view_cart_checkout()


@when("I proceed to checkout")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.proceed_to_checkout()


@then("I should be redirected to Sign-in Page")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    driver.verify_page()

