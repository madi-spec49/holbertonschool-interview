#!/usr/bin/python3
"""
Module pour calculer le périmètre d'une île dans une grille
"""


def island_perimeter(grid):
    """
    Renvoie le périmètre de l'île décrite dans la grille.
    """
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                # On ajoute les 4 côtés de la case de terre
                perimeter += 4

                # Si la case du dessus est de la terre, on retire 2 côtés
                if r > 0 and grid[r - 1][c] == 1:
                    perimeter -= 2

                # Si la case de gauche est de la terre, on retire 2 côtés
                if c > 0 and grid[r][c - 1] == 1:
                    perimeter -= 2

    return perimeter
