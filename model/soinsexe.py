from model.soins import *

potion =Soin("red velvelt", 50)
potion1 =Soin("blue dragon", 100)


print(f"j'ai trouver la potion {potion.get_name()}, et qui soigne les dégats à {potion.get_heal()}% ")
print(f"La potion {potion1.get_name()}, permet de se heal à {potion1.get_heal()}% ")