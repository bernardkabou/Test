def great_user(name=None):
    firstname = name if name else input("Veuillez entrer votre prénom : ")
    
    if firstname:
        print(f"Merci {firstname}) !")
    else:
        print("Vous n'avez pas saisi un prénom valide")
       
        