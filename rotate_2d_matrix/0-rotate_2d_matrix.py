#!/usr/bin/python3
"""
Module pour effectuer une rotation à 90 degrés d'une matrice 2D
"""


def rotate_2d_matrix(matrix):
    """
    Modifie une matrice n x n en place pour lui appliquer une rotation
    de 90 degrés dans le sens horaire.
    """
    n = len(matrix)

    # Étape 1 : Transposer la matrice (échanger matrix[i][j] et matrix[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Étape 2 : Inverser chaque ligne
    for i in range(n):
        matrix[i].reverse()
#!/usr/bin/python3
"""
Module pour effectuer une rotation à 90 degrés d'une matrice 2D
"""


def rotate_2d_matrix(matrix):
    """
    Modifie une matrice n x n en place pour lui appliquer une rotation
    de 90 degrés dans le sens horaire.
    """
    n = len(matrix)

    # Étape 1 : Transposer la matrice (échanger matrix[i][j] et matrix[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Étape 2 : Inverser chaque ligne
    for i in range(n):
        matrix[i].reverse()
