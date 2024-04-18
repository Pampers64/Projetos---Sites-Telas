#include <stdio.h>

int main() {
    int N, termo1 = 1, termo2 = 1, proximoTermo, i;

    printf("Digite o valor de N (maior ou igual a 2): ");
    scanf("%d", &N);

    printf("Sequencia de Fibonacci com %d termos:\n", N);

    
    printf("%d %d ", termo1, termo2);

    for (i = 3; i <= N; i++) {
        proximoTermo = termo1 + termo2;
        printf("%d ", proximoTermo);

        termo1 = termo2;
        termo2 = proximoTermo;
    }

    printf("\n");

    return 0;
}
