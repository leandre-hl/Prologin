# include <stdio.h>
# include <stdbool.h>
# include <stdlib.h>
# define int long long
# define MAX_P 1000
# define MAX_N 1000

void print_arr(int arr[], int length) {
    printf("Arr (size : %lld) : [", length);
    for (int i=0; i<length-1; i++) {
        printf("%lld, ", arr[i]);
    }
    printf("%lld]\n", arr[length-1]);
}

void swap(int arr[], int i, int j) {
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}

int partition(int* arr, int length) {
    int p = arr[0];
    int i, j;
    for (i=1, j=1; j<length; j++) {
        if (arr[j] < p) {
            swap(arr, i, j);
            i++;
        }
    }
    // Remettre le pivot en place
    swap(arr, 0, i-1);
    return i-1;
}

void quicksort(int* arr, int length) {
    int pivot = partition(arr, length);
    if (pivot>=2) {
        quicksort(arr, pivot);
    }
    if (pivot <= length-2) {
        quicksort(&(arr[pivot+1]), length-pivot-1);
    }
}


signed main() {
    int N, P;

    // Lire N et P
    scanf("%llu", &N);
    scanf("%llu", &P);

    // Lire les serrures
    int serrures[N];
    for (int i = 0; i < N; i++) {
        scanf("%llu", &serrures[i]);
    }
    quicksort(serrures, N);

    // Lire les clés
    int cles[P][N]; // Matrice pour stocker les P listes de N entiers
    for (int i = 0; i < P; i++) {
        for (int j = 0; j < N; j++) {
            scanf("%lld", &cles[i][j]);
        }
        quicksort(cles[i], N);
    }

    /*
    // Affichage pour vérifier les données lues
    printf("N = %lld, P = %lld\n", N, P);
    printf("Serrures : ");
    for (int i = 0; i < N; i++) {
        printf("%lld ", serrures[i]);
    }
    printf("\nClés :\n");
    for (int i = 0; i < P; i++) {
        for (int j = 0; j < N; j++) {
            printf("%lld ", cles[i][j]);
        }
        printf("\n");
    }
    */

    // Algo
    int arr[MAX_N];
    for (int i=0; i<N; i++) {
        arr[i] = 0;
    }
    for (int p=0; p<P; p++) {
        int i=0;
        for (int n=0; n<N ;) {
            if (i >= N) {break;}
            else if (cles[p][n]==serrures[i]) {arr[i]++; n++; i++;}
            else if (cles[p][n]>serrures[i]) {i++;}
            else {n++;}
        }
    }
    
    int valid = 0;
    for (int i=0; i<N; i++) {
        if (arr[i]==P) {
            valid++;
        }
    }
    printf("%lld\n", valid);

    for (int i=0; i<N; i++) {
        if (arr[i]==P) {
            printf("%lld ", serrures[i]);
        }
    }
    return 0;
}