from dotenv import load_dotenv
from web3 import Web3
from dotenv import load_dotenv
import os
import json

# ==========================================================

# CONFIGURATION

# ==========================================================

# load le .env
load_dotenv()

# URL RPC de la blockchain privée CPNV

RPC_URL = "http://10.229.43.182:8545"

# Adresse du compte expéditeur

SENDER_ADDRESS = "0x50496cb9D63347B77612e08b640F3A2B4e5B5A58"

# Clé privée (⚠ À améliorer !)

PRIVATE_KEY = os.getenv("PRIVATE_KEY")

# Montant à envoyer (en ETH)

AMOUNT_TO_SEND = 0.01

# ==========================================================

# CONNEXION À LA BLOCKCHAIN

# ==========================================================


w3 = Web3(Web3.HTTPProvider(RPC_URL))

if w3.is_connected():

    print("✅ Connecté à la blockchain")

else:

    print("❌ Connexion échouée")

    exit()


# ==========================================================

# LECTURE DES ADRESSES

# ==========================================================

def lire_adresses(fichier):
    """
    Lire les adresses Ethereum depuis un fichier texte
    Retourne une liste d’adresses valides
    """


    adresses = []

    with open(fichier, "r") as f:
        data = json.load(f)

    for adresse, name in data.items():

        # Vérifier que l’adresse est valide
        if w3.is_checksum_address(adresse):
            adresses.append((adresse, name))

    return adresses


# ==========================================================

# AFFICHER LES SOLDES

# ==========================================================

def afficher_soldes(adresses):
    """

    Affiche le solde de chaque adresse

    """

    for adresse ,name in adresses:
        balance_wei = w3.eth.get_balance(adresse)

        balance_eth = w3.from_wei(balance_wei, "ether")

        print(f"{adresse}, {name} : {balance_eth} ETH")


# ==========================================================

# ENVOI DE TRANSACTION

# ==========================================================

def envoyer_eth(destinataire, montant_eth, nonce):
    """

    Construit, signe et envoie une transaction

    """

    transaction = {

        "nonce": nonce,

        "to": destinataire,

        "value": w3.to_wei(montant_eth, "ether"),

        "gas": 21000,

        "gasPrice": w3.eth.gas_price,

        "chainId": w3.eth.chain_id

    }

    # Signature de la transaction

    signed_tx = w3.eth.account.sign_transaction(transaction, PRIVATE_KEY)

    # Envoi sur le réseau

    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

    return tx_hash.hex()


# ==========================================================

# PROGRAMME PRINCIPAL

# ==========================================================

def main():
    adresses = lire_adresses("adresse.json")

    print("\n=== Soldes avant envoi ===")

    afficher_soldes(adresses)

    # Récupération du nonce initial

    nonce = w3.eth.get_transaction_count(SENDER_ADDRESS)

    print("\n=== Envoi des transactions ===")

    for adresse, name in adresses:

        try:

            tx_hash = envoyer_eth(

                adresse,

                AMOUNT_TO_SEND,

                nonce

            )

            print(f"Transaction envoyée vers {adresse}")

            print(f"Hash : {tx_hash}")

            # Incrément du nonce

            nonce += 1



        except Exception as e:

            print(f"Erreur : {e}")

    print("\n=== Soldes après envoi ===")

    afficher_soldes(adresses)


if __name__ == "__main__":
    main()