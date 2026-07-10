#!/usr/bin/python3
"""
Module pour résoudre le problème du rendu de monnaie
"""


def makeChange(coins, total):
    """
    Détermine le nombre minimum de pièces nécessaires pour atteindre un total.
    """
    if total <= 0:
        return 0

    # Initialise un tableau de taille total + 1 avec une valeur "infinie" (total + 1)
    # Le pire des cas serait d'utiliser uniquement des pièces de 1, donc total pièces au max.
    dp = [total + 1] * (total + 1)

    # Il faut 0 pièce pour atteindre un total de 0
    dp[0] = 0

    # On calcule le nombre minimum de pièces pour chaque montant intermédiaire jusqu'au total
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # Si la valeur n'a pas été modifiée, c'est qu'on ne peut pas atteindre le total
    return dp[total] if dp[total] != total + 1 else -1