#include <stdio.h>

int main() {
    int numero, soma;

    soma = 0;

    for (numero = 1; numero <= 500; numero++) {
        if (numero % 2 != 0) {  
            soma += numero;     
        }
    }

    printf("A soma dos numeros impares de 1 a 500: %d\n", soma);

    return 0;
}
