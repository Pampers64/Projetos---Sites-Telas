#include <stdio.h>
#include <math.h>

int main()

{
    double x, soma = 0, termo;
   
    printf("Digite um valor para x: ");
    scanf("%lf", &x);

    for (int i = 0; i < 15; i++) 
	{
        termo = i + pow(x, i + 1);
        soma += termo;
    }

    printf("A soma dos 15 primeiros termos da série é: %.2lf\n", soma);

    return 0;
}
