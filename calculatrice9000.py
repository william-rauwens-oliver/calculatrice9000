def afficher_historique(historique):
    if historique:
        print("\nHistorique des opérations :")
        for i, operation in enumerate(historique, 1):
            print(f"{i}. {operation}")
    else:
        print("\nHistorique vide")

def historique_effacer(historique):
    historique.clear()
    print("L'historique a bien été effacé")

def effectuer_operation(num1, num2, operation, historique):
    try:
        if operation not in {"+", "-", "*", "/"}:
            raise ValueError("Opération non-valide")
        if operation == "/" and num2 == 0:
            raise ValueError("Il n'est pas possible de faire une division par 0")
        if operation == "+":
            resultat = num1 + num2
        elif operation == "-":
            resultat = num1 - num2
        elif operation == "*":
            resultat = num1 * num2
        elif operation == "/":
            resultat = num1 / num2
        print(f"Le résultat de l'opération est : {resultat}")
        historique.append(f"{num1} {operation} {num2} = {resultat}")
    except ValueError as erreur:
        print(f"Erreur : {erreur}")
    except Exception as erreur:
        print(f"Erreur détectée : {erreur}")

def calculatrice():
    historique = []
    try:
        num1 = float(input("Entrez le premier nombre : "))
        num2 = float(input("Entrez le deuxième nombre : "))
        operation = input("Entrez le mode d'opération choisi (+, -, /, *) : ")
        effectuer_operation(num1, num2, operation, historique)
        choix = input("\nSouhaitez-vous afficher l'historique (o) ou l'effacer ? (n) (Appuyez sur entrée pour continuer !) : ")
        if choix.lower() == "o":
            afficher_historique(historique)
            choix_suppression = input("\nVoulez-vous supprimer l'historique ? (o/n) : ") # j'ai ajouté un input qui re-demande dans le terminal si on veut supprimer l'historique apres avoir demandé de le voir !
            if choix_suppression.lower() == "o":
                historique_effacer(historique)

    except ValueError as erreur_saisie:
        print(f"Erreur : {erreur_saisie}")
    except Exception as autre_erreur:
        print(f"Erreur détectée : {autre_erreur}")

calculatrice()