# Banking application sample

## Usage

`python3 main.py`

## `main.py` Overview

The `main.py` file serves as the entry point to the Banking System application, orchestrating the overall flow and interactions between different layers of the application in accordance with Clean Architecture principles. Its primary responsibilities include initializing the application's environment, setting up dependencies, and providing a user interface for interaction with the system.

## Demonstration of Core Functionalities

### Creating Customer and Account

The script demonstrates creating a new customer and associated account with `create_account` method from the `AccountManagementUseCase`. It doesn't explicitly show customer creation but implies it's handled within the `create_account` method. The account creation process assigns a unique identifier (customer ID) and account number to the new account, simulating the onboarding of a new customer.

### Executing Transactions

The script then demonstrates making transactions on the newly created account. It deposits an amount of 100 units into the account and then withdraws 50 units. The `TransactionUseCase` handles these operations, updating the account's balance accordingly. Error handling for insufficient balance is demonstrated using a try-except block, catching `InsufficientBalanceError` if a withdrawal attempt exceeds the account's balance.

### Generating Account Statement

Finally, the script generates an account statement using the `AccountStatementUseCase`. This statement likely includes the account's transaction history and current balance, although the specific format of the statement isn't detailed in the script.
