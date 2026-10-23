[🇫🇷 Français](README.fr.md) | [🇬🇧 English](README.md)

# Prologin

Mes solutions à des exercices de [Prologin](https://prologin.org/), le concours français d'informatique. Les énoncés sont en français et se trouvent sur le site de Prologin. Les solutions sont écrites en C et en Python.

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
