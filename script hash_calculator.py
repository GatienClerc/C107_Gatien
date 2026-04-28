#!/usr/bin/env python3

import hashlib
from pathlib import Path


def sha256_from_text(text: str) -> str:
    """Calcule le hash SHA-256 d'un texte."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def sha256_from_file(file_path: Path) -> str:
    """Calcule le hash SHA-256 d'un fichier (lecture binaire)."""
    sha256 = hashlib.sha256()
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()


def save_hash_to_file(hash_value: str, output_file: str = "hash_output.txt") -> None:
    """Sauvegarde le hash dans un fichier texte."""
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(hash_value + "\n")


def ask_save_result(hash_value: str) -> None:
    """Propose à l'utilisateur de sauvegarder le résultat."""
    choice = input("Souhaitez-vous sauvegarder le hash dans 'hash_output.txt' ? (o/n) : ").strip().lower()
    if choice == "o":
        save_hash_to_file(hash_value)
        print("✅ Hash sauvegardé dans hash_output.txt")


def main() -> None:
    while True:
        print("")
        print("--- Calculateur de hash SHA-256 ---")
        print("[1] Hachage d’un texte saisi")
        print("[2] Hachage d’un fichier texte")

        choice = input("Votre choix : ").strip()

        try:
            if choice == "1":
                text = input("Entrez le texte à hacher : ").strip()
                if not text:
                    raise ValueError("Le texte saisi est vide.")
                print(repr(text))
                hash_value = sha256_from_text(text)
                print(f"\nHash SHA-256 :\n{hash_value}")
                ask_save_result(hash_value)

            elif choice == "2":
                path_input = input("Entrez le chemin du fichier : ").strip()
                if not path_input:
                    raise ValueError("Chemin de fichier vide.")

                file_path = Path(path_input)


                if not file_path.exists():
                    raise FileNotFoundError("Le fichier spécifié est introuvable.")

                if not file_path.is_file():
                    raise ValueError("Le chemin ne correspond pas à un fichier valide.")

                hash_value = sha256_from_file(file_path)
                print(f"\nHash SHA-256 du fichier :\n{hash_value}")
                ask_save_result(hash_value)

            else:
                print("❌ Choix invalide. Veuillez sélectionner [1] ou [2].")

        except FileNotFoundError as e:
            print(f"❌ Erreur : {e}")
        except ValueError as e:
            print(f"❌ Erreur : {e}")
        except Exception as e:
            print(f"❌ Erreur inattendue : {e}")


if __name__ == "__main__":
    main()