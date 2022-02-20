# PART 1: Inputs to the whole exercise
from time import sleep
# Note for the following two imports we need to have run: `pip install web3 pandas openpyxl`
from web3 import Web3
import pandas as pd

# You will want to choose a more reliable node in production if you run this under load
node = "https://cloudflare-eth.com"
# Target addresses to watch. Note you can extend this list
addresses = [
    "0x3845badAde8e6dFF049820680d1F14bD3903a5d0"
]
# Wallet addresses to scan - note that they should be in checksum format, which means those uppercase and lowercase letters
wallets = [
    "0xfF08F103A63A653D518bD9f8A837b795c6f110c3",
    "0xfF08F103A63A653D518bD9f8A837b795c6f110c3",
    "0xfF08F103A63A653D518bD9f8A837b795c6f110c3",
    "0xfF08F103A63A653D518bD9f8A837b795c6f110c3"
]

# PART II: Code to make it work

# Connecy
web3 = Web3(Web3.HTTPProvider(node))
while (True):
    try: 
        web3.isConnected()
        break
    except:
        sleep(0.1)

for address in addresses:
    # Get the contract. Note that we need the ABI loaded in for functions to work
    abi_path = "./erc20.abi.json"
    abi = open(abi_path).read()
    contract = web3.eth.contract(abi=abi, address=address)

    # Fetch balances for all wallets you are tracking
    balances = []
    for wallet in wallets:
        balance = contract.functions.balanceOf(wallet).call()
        balances.append([wallet, balance])

    # Bonus: Export to its own sheet in Excel file
    df = pd.DataFrame(balances)#.iloc[:,1:]
    with pd.ExcelWriter("./output.xlsx", mode='a', if_sheet_exists='replace') as writer:
        df.to_excel(
            writer, 
            sheet_name=address, 
            header=["Wallet", "Balance"], 
            
        
        )