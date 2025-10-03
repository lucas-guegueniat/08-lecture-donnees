"""Lucas Guéguéniat - 08-lecture-donnees"""

#### Imports et définition des variables globales

import csv

FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    l = []
    with open(filename, 'r', encoding="utf8") as f:
        r = csv.reader(f, delimiter=';')
        l = list(r)
        l = [[int(i) for i in l[j]] for j in range(len(l))]
    return l

def get_list_k(data, k):
    """Retourne la k-ième liste
    """
    l = data
    return l[k]

def get_first(l):
    """Retourne le premier élément de la liste en argument
    """
    return l[0]

def get_last(l):
    """Retourne le dernier élément de la liste en argument
    """
    return l[-1]

def get_max(l):
    """Retourne la valeur max de la liste
    """
    return max(l)

def get_min(l):
    """Retourne la valeur min de la liste
    """
    return min(l)

def get_sum(l):
    """Retourne la somme des éléments de la liste
    """
    s = 0
    for i in l:
        s = s + i
    return s


#### Fonction principale


def main():
    """Fonction principale appelant et vérifiant les autres fonctions
    """
    data = read_data(FILENAME)
    for i, l in enumerate(data):
        print(i, l)
    k = 37
    print(k, get_list_k(data, 37))
    print(get_sum(data[k]))


if __name__ == "__main__":
    main()
