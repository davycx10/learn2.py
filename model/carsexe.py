from model.cars import *

ma_voiture =Cars("ferrari", "Blanche")
autre_voiture =Cars("aston martin", "Noir")


print(f"j'ai une voiture de la marque, {autre_voiture.get_marque()}, et qui est de couleur, {autre_voiture.get_couleur()}")
print("j'ai une voiture de la marque", {ma_voiture.get_marque()}, "qui est de couleur", ma_voiture.get_couleur(), "et qui roule à", ma_voiture.get_rouler(), "km/h")
#print("je ralenti", ma_voiture.get_freiner())