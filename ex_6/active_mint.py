from dotenv import load_dotenv
from web3 import Web3
import os
import json

# ==========================================================

# CONFIGURATION

# ==========================================================

load_dotenv()

# URL RPC de la blockchain privée CPNV

RPC_URL = "http://10.229.43.182:8545"

# Adresse du compte expéditeur

SENDER_ADDRESS = "0x50496cb9D63347B77612e08b640F3A2B4e5B5A58"

# Clé privée

PRIVATE_KEY = os.getenv("PRIVATE_KEY")

contract_address = "0x5b771ee0c0246Fbd2C54c4037bEA259ED8c43490"

w3 = Web3(Web3.HTTPProvider(RPC_URL))

if w3.is_connected():

    print("✅ Connecté à la blockchain")

else:

    print("❌ Connexion échouée")

    exit()

account = w3.eth.account.from_key(PRIVATE_KEY)

with open("ClercMintContract.abi", "r") as abi_file:
    abi = json.load(abi_file)

# Créer instance du contrat
contract = w3.eth.contract(
    address=contract_address,
    abi=abi
)

# Build transaction
tx = contract.functions.toggleIsMintEnabled().build_transaction({
    "from": account.address,
    "nonce": w3.eth.get_transaction_count(account.address),
    "gas": 100000,
    "gasPrice": w3.eth.gas_price,
})

# Sign and send
signed_tx = w3.eth.account.sign_transaction(tx, PRIVATE_KEY)
tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

print("Transaction hash:", tx_hash.hex())

# Wait for confirmation
receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
print("Block:", receipt.blockNumber)

# Verify state
enabled = contract.functions.isMintEnabled().call()
print("isMintEnabled =", enabled)
