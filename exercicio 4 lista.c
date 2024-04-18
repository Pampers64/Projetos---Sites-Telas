#include <stdio.h>

int Triangular(int n) {
    int i = 1;
    int j = 2;
    int k = 3;

    while (i * j * k <= n) {
        if (i * j * k == n) {
            return 1; 
        }
        i++;
        j++;
        k++;
    }

    return 0; 
}

int main() {
    int n;

    printf("Digite um número natural: ");
    scanf("%d", &n);

    if (Triangular(n)) {
        printf("%d é um número triangular.\n", n);
    } else {
        printf("%d não é um número triangular.\n", n);
    }

    return 0;
}
