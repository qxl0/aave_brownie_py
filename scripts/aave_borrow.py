from scripts.helpful_scripts import get_account
from brownie import network, config, interface
from scripts.get_weth import get_weth
from web3 import Web3


# 0.1
amount = 100000000000000000

def main():
  account = get_account()
  erc20_address = config["networks"][network.show_active()]["weth_token"]
  if network.show_active() in ["mainnet-fork-dev"]:
    get_weth()
  lending_pool = get_lending_pool()
  print(lending_pool)
  approve_erc20(amount,lending_pool.address, erc20_address, account)
  print("Depositing....")
  tx = lending_pool.deposit(erc20_address, amount, account.address, 0, {"from": account})
  tx.wait(1)
  print("Deposited!")

def approve_erc20(amount, spender, erc20_address, account):
  print("Approving ERC20 token....")
  erc20 = interface.IERC20(erc20_address)
  tx = erc20.approve(spender, amount, {"from": account})
  tx.wait(1)
  print("Approved")
  return tx
  # ABI
  # address

def get_lending_pool():
  # ABI
  # Address
  lending_pool_addresses_provider = interface.ILendingPoolAddressesProvider(
    config["networks"][network.show_active()]["lending_pool_addresses_provider"]
  )
  lending_pool_address = lending_pool_addresses_provider.getLendingPool()
  lending_pool = interface.ILendingPool(lending_pool_address)
  return lending_pool