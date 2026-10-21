# include <stdio.h>
# include <stdbool.h>
# include <stdlib.h>
# include <math.h>
# define int long long
# define MAX_N 1000


signed main () {
    int N, D;

    // Lire N et D
    scanf("%llu", &N);
    scanf("%llu", &D);

    // Lire les loqueteaux
    int lock[MAX_N];
    for (int i = 0; i < N; i++) {
        scanf("%llu", &lock[i]);
    }
    /*
    // Affichage pour vérifier les données lues
    printf("N = %lld, D = %lld\n", N, D);
    printf("Lock : ");
    for (int i = 0; i < N; i++) {
        printf("%lld ", lock[i]);
    }
    printf("\n");
    */

    // Algo
    for (int i=0; i<D; i++) {
        int count_0 = 0;
        for (int j=i; j < N; j+=D) {
            if (lock[j]==0) {
                count_0++;
            }
        }
        int expected_0;
        if (i >= N / 2) {
            expected_0 = 0;
        } else {
            expected_0 = ((N / 2) - i) / D + (((N / 2) + D - i) % D != 0);
        }

        if (count_0 != expected_0) {
            printf("NON");
            return 0;
        }
    }
    printf("OUI");
    return 0;
}