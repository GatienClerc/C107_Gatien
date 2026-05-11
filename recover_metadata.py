from web3 import Web3
from web3.middleware import ExtraDataToPOAMiddleware
import json

RPC_URL = "http://10.229.43.182:8545"

w3 = Web3(Web3.HTTPProvider(RPC_URL))
w3.middleware_onion.inject(ExtraDataToPOAMiddleware, layer=0)

print("✅ Connecté :", w3.is_connected())

def get_data(tx_hash):
    tx = w3.eth.get_transaction(tx_hash)

    print(tx)
    data_hex = tx["input"]

    if not data_hex or data_hex == "0x":
        return "Aucune donnée"

    decoded = Web3.to_text(hexstr=data_hex.hex())
    return decoded
print(get_data("f691d6d61a683b442f3916d7540b6cdf6d826593e299cc340cec0832e9ca8447"))