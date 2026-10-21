[🇫🇷 Français](README.fr.md) | [🇬🇧 English](README.md)

# Prologin

Mes solutions à des exercices de [Prologin](https://prologin.org/), le concours français d'informatique. Les énoncés sont en français et se trouvent sur le site de Prologin. Les solutions sont écrites en C, avec une en Python.

## Fichiers

| Fichier | Langage | Rôle |
|---------|---------|------|
| `2022_2_assemblage_cles.c` | C | Lit une liste de serrures et plusieurs listes de clés, puis affiche le nombre de valeurs présentes à la fois dans les serrures et dans chaque liste de clés, suivi de ces valeurs. Utilise un quicksort maison, puis compare les listes triées en un seul passage. |
| `2022_2_porte_derobee.c` | C | Copie de la solution précédente qui ne compile pas seule (voir les remarques ci-dessous). |
| `2022_3_loqueteaux.c` | C | Vérifie la configuration des loqueteaux donnée en entrée et affiche `OUI` ou `NON`. |
| `2022_4_flechettes.c` | C | Affiche la somme maximale d'une sous-séquence contiguë des valeurs du mur, grâce à l'algorithme de Kadane en O(N). |
| `2023_3_sabotage.py` | Python | Combine une recherche dichotomique sur la réponse et un parcours en profondeur (DFS) d'un arbre, puis affiche la plus petite valeur valide. |
| `utilities.c` | C | Fonctions utilitaires réutilisables d'une solution à l'autre : création de tableaux dynamiques, affichage de tableaux, `swap` et un quicksort. |

## Utilisation

Tous les programmes lisent leur entrée sur l'entrée standard, selon le format de Prologin, et écrivent la réponse sur la sortie standard.

```bash
# Solutions en C
gcc -O2 2022_4_flechettes.c -o flechettes
./flechettes < input.txt

# Solution en Python
python3 2023_3_sabotage.py < input.txt
```

Exemple avec `2022_4_flechettes.c` (la première ligne donne le nombre de valeurs, la seconde les valeurs elles-mêmes) :

```
$ printf '5\n1 -2 3 4 -1\n' | ./flechettes
7
```

## Remarques

- Tous les programmes C utilisent `#define int long long` pour éviter les dépassements d'entiers. C'est pourquoi `main` est déclaré `signed main()`.
- `2022_2_porte_derobee.c` ne compile pas seul : il appelle `quicksort`, qui n'est défini que dans `2022_2_assemblage_cles.c`.
- `utilities.c` ne compile pas non plus, car `swap` y est défini deux fois. Supprimez l'une des deux définitions pour corriger le problème.
- Les fonctions de `utilities.c` sont destinées à être copiées dans une solution en cas de besoin.