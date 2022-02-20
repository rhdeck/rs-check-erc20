# rs-check-erc20
 Check balances of a wallet in ERC 20 with web3.py

 ## Prerequisites
 1. Reasonably current Python (3.9 or newer is best)
 2. PyPi packages installed in scope:
    1. `web3` 
    2. `pandas` 
    3. `openpyxl`


## Installation
1. Make sure you have the prerequisites either globally installed or, if you have pipenv, run `pipenv install`
2. That's about it. Run `python main.py` or `pipenv run python main.py` to scan the contract and generate the `output.xlsx` workbook with appropriate sheets

## Updating
This is designed for learning, so view `main.py` to see the inputs. Note that this script does not take command line arguments at this time.
