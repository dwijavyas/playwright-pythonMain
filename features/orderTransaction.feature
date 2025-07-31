Feature: Order Transactions
    Tests related to Order Transactions

    Scenario Outline: Verify Order Success message shown in details page
     Given place the item order with <username> and <password>
     And the user in on landing page
     When I login to portal with <username> and <password>
     And navigate to Orders page
     And select the OrderID
     Then verify the order message 

     Examples:
     |          username     |  password   |
     | rahulshetty@gmail.com | Iamking@000 |
