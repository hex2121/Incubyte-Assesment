Feature: User Registration and Authentication
  As a new user
  I want to create an account and log in
  So that I can access my account

  Scenario: New user registration
    Given I am on the home page
    When I click on create account
    And I enter my registration details
    Then I should be successfully registered

  Scenario: User login
    Given I am a registered user
    When I enter my login credentials
    Then I should be successfully logged in