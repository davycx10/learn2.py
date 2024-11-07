from batiment import *

batiment = Batiment(5, "rue d'azur", "Xia")
print(f"\n le bâtiment {batiment.get_noms()}, a {batiment.get_étage()} d'étages, et se trouve à {batiment.get_adresse()}. \n\n")

immeuble1 = Immeuble(6, "122 rue d'azur", "villa du vent", 2)
print(f"l'immeuble {immeuble1.get_noms()}, à {immeuble1.get_étage()} d'étages, elle a aussi {immeuble1.get_balcons()} balcons. L'immeuble se trouve au {immeuble1.get_adresse()}.")

immeuble2 = Immeuble(12, "124 rue d'azur", "Cimes d'Azur", 8)
print(f"l'immeuble {immeuble2.get_noms()}, à {immeuble2.get_étage()} d'étages, elle a aussi {immeuble2.get_balcons()} balcons. L'immeuble se trouve au {immeuble2.get_adresse()}. ")

immeuble3 = Immeuble(9, "125 rue d'azur", "résidence rouge", 7)
print(f"l'immeuble {immeuble3.get_noms()}, à {immeuble3.get_étage()} d'étages, elle a aussi {immeuble3.get_balcons()} balcons. L'immeuble se trouve au {immeuble3.get_adresse()}. ")

immeuble = Immeuble(10, "123 rue d'azur", "résidence des étoiles", 5)
print(f"l'immeuble {immeuble.get_noms()}, à {immeuble.get_étage()} d'étages, elle a aussi {immeuble.get_balcons()} balcons. L'immeuble se trouve au {immeuble.get_adresse()}. \n\n")

supermarket = Supermarket(2, "10 rue d'azur", "supermark", 10, 2)
print(f"Le supermarché qui se trouve au {supermarket.get_adresse()}, se nomme {supermarket.get_noms()}. Le magasin possède {supermarket.get_étage()} d'étages, avec {supermarket.get_rayons()} rayons et {supermarket.get_réserve()} réserves.")

supermarket1 = Supermarket(3, "1 rue gosh", "Supemark", 15, 4)
print(f"Le supermarché qui se trouve au {supermarket1.get_adresse()}, se nomme {supermarket1.get_noms()}. Le magasin possède {supermarket1.get_étage()} d'étages, avec {supermarket1.get_rayons()} rayons et {supermarket1.get_réserve()} réserves.")

banque = Bank(3, "140 rue gosh", "ICC", 12)
print(f"la banque {banque.get_noms()}, possède {banque.get_coffre()} coffres-fort, et {banque.get_étage()} étages. La banque se situe au {banque.get_adresse()}. \n\n")