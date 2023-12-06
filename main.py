def demande():    
    nb1 = input("Calculatrice9000 ! Quel est votre premier nombre ? ")
    try:
        nb1 = float(nb1)
    except:
        print("Veuillez insérer un nombre")
        demande()

    operator = input("Quelle opération voulez vous effectuer ? (+, -, /, *) ")
    if operator not in ["+","-","*","/","%"]:
        print("Veuillez insérer un opérateur valide")
        demande()
    nb2 = input("Votre deuxième nombre : ")
    try:
        nb2 = float(nb2)
    except:
        print("Veuillez insérer un nombre")
        demande()
    if operator == "+":
        print(f"Résultat : {nb1+nb2}")
        demande()
    if operator == "-":
        print(f"Résultat : {nb1-nb2}")
        demande()
    if operator == "*":
        print(f"Résultat : {nb1*nb2}")
        demande()
    if operator == "/":
        print(f"Résultat : {nb1/nb2}")
        demande()
    if operator == "%":
        print(f"Résultat : {nb1%nb2}")
        demande()

demande()