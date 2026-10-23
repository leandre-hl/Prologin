[🇫🇷 Français](README.fr.md) | [🇬🇧 English](README.md)

# Prologin

My solutions to exercises from [Prologin](https://prologin.org/), the French computer science contest. The problem statements are in French and can be found on the Prologin website. Solutions are written in C and in Python.

## Usage

All programs read their input from the standard input, following the Prologin format, and print the answer to the standard output.

```bash
# C solutions
gcc -O2 2022_4_flechettes.c -o flechettes
./flechettes < input.txt

# Python solution
python3 2023_3_sabotage.py < input.txt
```

Example with `2022_4_flechettes.c` (the first line is the number of values, the second line the values themselves):

```
$ printf '5\n1 -2 3 4 -1\n' | ./flechettes
7
```
