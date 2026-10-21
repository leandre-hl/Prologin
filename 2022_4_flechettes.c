# include <stdlib.h>
# include <stdio.h>
# include <stdbool.h>
# define int long long
# define MAX_N 100000
# define MAX_M 1000000
# define MIN_M -1000000

int max(int a, int b) {
    return (a > b)? a : b;
}

signed main() {
    int N;
    scanf("%lld", &N);

    int mur[MAX_N];
    int cumsum[MAX_N];
    int lst = 0;
    for (int i=0; i<N; i++) {
        scanf("%lld", &mur[i]);
        cumsum[i] = mur[i] + lst;
        lst = cumsum[i];
    }
    // Algorithme de Kadane pour trouver la sous somme maximale
    int max_sous_somme = MIN_M;
    int current_max_sous_somme = 0;

    for (int i=0; i<N; i++) {
        current_max_sous_somme = max(mur[i], current_max_sous_somme + mur[i]);
        max_sous_somme = max(max_sous_somme, current_max_sous_somme);
    }

    printf("%lld\n", max_sous_somme);


    return 0;
}
