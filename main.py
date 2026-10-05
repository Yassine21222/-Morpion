plateau = [" " for _ in range(9)]
joueurs = ["❌", "⭕"]
tour = 0

positions_gagnantes = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


def afficher():
    print()
    for ligne in range(3):
        debut = ligne * 3
        print(f" {plateau[debut]} | {plateau[debut + 1]} | {plateau[debut + 2]} ")

        if ligne < 2:
            print("---+---+---")
    print()


def victoire(symbole):
    for combinaison in positions_gagnantes:
        a, b, c = combinaison

        if plateau[a] == symbole and plateau[b] == symbole and plateau[c] == symbole:
            return True

    return False


def plateau_complet():
    return " " not in plateau


while True:
    afficher()

    symbole = joueurs[tour % 2]

    while True:
        try:
            choix = int(input(f"Joueur {symbole}, choisis une case de 1 à 9 : "))

            if choix < 1 or choix > 9:
                print("Choisis un nombre entre 1 et 9.")
            elif plateau[choix - 1] != " ":
                print("Cette case est déjà prise.")
            else:
                break

        except ValueError:
            print("Entre seulement un nombre.")

    plateau[choix - 1] = symbole

    if victoire(symbole):
        afficher()
        print(f"Le joueur {symbole} a gagné !")
        break

    if plateau_complet():
        afficher()
        print("Match nul !")
        break

    tour += 1