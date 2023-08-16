taille = float(input("Entrez votre taille: "))
sexe = str(input("Entrez votre sexe: "))

if sexe == "homme":
    ideal_wheight1 = (72.7 * taille) - 58
    print(f"Seu peso ideal deve ser {ideal_wheight1:.1f}")
elif sexe == "femme":
    ideal_wheight2 = (62.1 * taille) - 44.7
    print(f"Seu peso ideal deve ser {ideal_wheight2:.1f}")
else:
    print("Digite 'homme' ou 'femme'.")


