#!/usr/bin/python3
"""
Script de parsing de log en temps réel via stdin.
Calcule la taille totale des fichiers et compte les codes de statut HTTP.
"""
import re
import sys


def print_statistics(total_size, status_codes):
    """
    Affiche les statistiques accumulées jusqu'à présent.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    total_size = 0
    line_count = 0

    # Dictionnaire pour suivre uniquement les codes de statut autorisés
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    # Expression régulière pour valider strictement le format d'entrée demandé
    # Format attendu : <IP> - [<date>] "GET /projects/260 HTTP/1.1" <status> <size>
    log_pattern = re.compile(
        r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - "  # Adresse IP
        r"\[.*?\] "                                 # Date entre crochets
        r"\"GET /projects/260 HTTP/1.1\" "          # Requête exacte
        r"(\d{3}) "                                 # Groupe 1 : Code statut (3 chiffres)
        r"(\d+)$"                                   # Groupe 2 : Taille du fichier (entier)
    )

    try:
        for line in sys.stdin:
            line = line.strip()
            match = log_pattern.match(line)

            # Si la ligne ne correspond pas au format requis, elle est ignorée
            if not match:
                continue

            # Extraction des données validées
            status_code = match.group(1)
            file_size = int(match.group(2))

            # Accumulation de la taille du fichier
            total_size += file_size

            # Incrémentation du code statut s'il fait partie de la liste attendue
            if status_code in status_codes:
                status_codes[status_code] += 1

            line_count += 1

            # Toutes les 10 lignes valides, on affiche les statistiques
            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

        # Si l'entrée se termine proprement sans atteindre un multiple de 10
        print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        # Interception du CTRL+C : affichage des stats avant de relancer l'exception
        print_statistics(total_size, status_codes)
        raise

 
if __name__ == "__main__":
    main()
