[🇫🇷 Français](README.fr.md) | [🇬🇧 English](README.md)

# Prologin

My solutions to exercises from [Prologin](https://prologin.org/), the French computer science contest. The problem statements are in French and can be found on the Prologin website. Solutions are written in C, plus one in Python.

## Files

| File | Language | What it does |
|------|----------|--------------|
| `2022_2_assemblage_cles.c` | C | Reads a list of locks and several lists of keys, and prints how many values appear in the locks and in every key list, followed by those values. Sorts with a custom quicksort and compares the sorted lists in a single pass. |
| `2022_2_porte_derobee.c` | C | Copy of the previous solution that does not compile on its own (see notes below). |
| `2022_3_loqueteaux.c` | C | Checks the latch configuration given as input and prints `OUI` or `NON`. |
| `2022_4_flechettes.c` | C | Prints the maximum sum of a contiguous sub-sequence of the wall values, using Kadane's algorithm in O(N). |
| `2023_3_sabotage.py` | Python | Binary search on the answer combined with a depth-first search over a tree, and prints the smallest valid value. |
| `utilities.c` | C | Helper functions reused across solutions: dynamic array creation, array printing, `swap`, and a quicksort. |

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

## Notes

- All C programs use `#define int long long` to avoid integer overflows. This is why `main` is declared as `signed main()`.
- `2022_2_porte_derobee.c` does not compile on its own: it calls `quicksort`, which is only defined in `2022_2_assemblage_cles.c`.
- `utilities.c` does not compile either, because `swap` is defined twice. Remove one of the two definitions to fix it.
- The helpers in `utilities.c` are meant to be copied into a solution when needed.