
## Introduction

BugetFlow is a desktop application designed to automate the manual process of dividing a paycheck across multiple accounts. Instead of recalculating with a calculator each time, the user can define their accounts once, assign each a fixed dollar amount or a percentage, and instantly see how their paycheck is split. The application was built for personal use to save time and reduce errors in day-to-day money management.

## Users

They BudgetFlow is intended for any individual who earns an income and wants to automate how they divide their money across multiple accounts. No technical knowledge is required. The only skills needed are basic computer operation, using a mouse and keyboard.

## Functional Requirements

*This system shall:*
1. Accept a total paycheck amount entered by the user
2. Allow the user to add multiple accounts with a name, and fixed dollar amount or percentage
3. Calculate each account's split by subtracting fixed amounts first, and then applying percentage  to the remainder
4. Validate that all amounts account for 100% of the total with no remainder
5. Display the calculated result for each account
6. Allow the user to add, rename, edit, and delete accounts
7. Automatically save all accounts to a local JSON file and reload them when the application is launched

## Non-Functional Requirements

*This system shall:*
1. Provide a simple and intuitive user interface  that requires no learning curve
2. Only accept numerical values in amount fields, rejecting any non-numeric input
3. Prevent the user from creating an account without a name
4. Respond to user actions immediately with no noticeable delay

## Constraints
1. The application is built using python and Tkinter library
2. The application is currently designed for Windows only
3. macOS supports is planned for a future version

## Future Features
1. Sub-accounts - The ability to create accounts nested under a main account
2. macOS support