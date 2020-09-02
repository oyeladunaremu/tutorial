Feature: Guest Shopping
  As a shopper,
  I should be able to shop on any site,
  So that i can checkout my item

  Scenario: Shopping on Jumia

    Given I am on "jumia" website

    And I search for an item

    And I click on search button

    And I select an item

    And I added the item to cart

    And I click on view cart and checkout

    When I proceed to checkout

  Then I should be redirected to Sign-in Page

    
