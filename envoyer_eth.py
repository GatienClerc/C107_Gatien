from web3 import Web3
from dotenv import load_dotenv

import os

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

AMOUNT_TO_SEND = 0.1

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

    Retourne une liste d’adresses

    """

    adresses = []

    with open(fichier, "r") as f:

        for ligne in f:

            adresse = ligne.strip()

            # Vérifier que l’adresse est valide

            if __________________________:
                adresses.append(adresse)

    return adresses


# ==========================================================

# AFFICHER LES SOLDES

# ==========================================================

def afficher_soldes(adresses):
    """

    Affiche le solde de chaque adresse

    """

    for adresse in adresses:
        balance_wei = ________________________

        balance_eth = ________________________

        print(f"{adresse} : {balance_eth} ETH")


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

        "value": ____________________________,

        "gas": ______________________________,

        "gasPrice": _________________________,

        "chainId": __________________________

    }

    # Signature de la transaction

    signed_tx = _______________________________

    # Envoi sur le réseau

    tx_hash = _________________________________

    return tx_hash.hex()


# ==========================================================

# PROGRAMME PRINCIPAL

# ==========================================================

def main():
    adresses = lire_adresses("adresses.txt")

    print("\n=== Soldes avant envoi ===")

    afficher_soldes(adresses)

    # Récupération du nonce initial

    nonce = __________________________________

    print("\n=== Envoi des transactions ===")

    for adresse in adresses:

        try:

            tx_hash = envoyer_eth(

                adresse,

                AMOUNT_TO_SEND,

                nonce

            )

            print(f"Transaction envoyée vers {adresse}")

            print(f"Hash : {tx_hash}")

            # Incrément du nonce

            nonce += _______



        except Exception as e:

            print(f"Erreur : {e}")

    print("\n=== Soldes après envoi ===")

    afficher_soldes(adresses)


if __name__ == "__main__":
    main()