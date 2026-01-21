import random

#definieer een functie die een willekeurige nucleotide base teruggeeft
def get_random_base():
    keuze = random.randint(1, 4)

    if keuze == 1:
        return "Ade"
    elif keuze == 2:
        return "Cyt"
    elif keuze == 3:
        return "Gua"
    else:
        return "Thy"
    
base1 = "Gua"
base2 = "Cyt"
base3 = "Thy"
base4 = "Gua"
base5 = "Ade"

num_mutaties = random.randint(1, 3)

# muteer een willekeurig aantal bases in de DNA sequentie.
for mutation in range(num_mutaties):
    base_positie = random.randint(1, 5)
    new_base = get_random_base()

    if base_positie == 1:
        base1 = new_base
    elif base_positie == 2:
        base2 = new_base
    elif base_positie == 3:
        base3 = new_base
    elif base_positie == 4:
        base4 = new_base
    elif base_positie == 5:
        base5 = new_base

print(base1 + base2 + base3 + base4 + base5)
