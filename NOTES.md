## Project Description
A python Tkinter application that helps users split their paycheck into different accounts such as checking, savings, and investments.

Users can allocate money using either fixed amounts or percentages. Accounts can also contain sub-accounts to further divide funds (e.g., investments split into stocks and crypto)
## Features
- Enter total paycheck amount
- Add, rename, and delete accounts
- Accounts can use:
	- Fixed dollar amount
	- Percentage of remaining funds
- Optional sub-accounts for further splitting
- Calculate and display distribution
- Simple graphical interface using Tkinter
## Example Use Case
```py
Total paycheck: $2000
Accounts:
	checking: $500(fixed)
	savings: 30%
	investment: 20%
	
	investment sub-accounts:
		stocks: 50%
		crypto: 50%
		
		
		
Result:
Checking: $500
Savings: $450
Investment: $300

Stocks: $150
Crypto: $150
```
## Data Structure
```python
accounts = [
{
"name":"Checking",
"type":"fixed",
"sub_accounts":[]
}
{
"name":"Invesment",
"type":"fixed",
"value":500,
"sub_accounts":[
{"name":"Stocks","percent":50},
{"name":"Crpyto","percent":50}]
}
```
## Development Plan
Step 1: Build basic Tkinter window
Step 2: Implement dynamic accounts list
Step 3: Add account management (add, rename, delete)
Step 4: Implement fixed and percentage calculations
Step 5: Add sub-account support
Step 6: Improve user interface