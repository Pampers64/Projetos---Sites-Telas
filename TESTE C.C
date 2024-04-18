#include<stdio.h>
#include<stdlib.h>
	int main ()
	{
		float valor1, valor2, valor3, media; 
		
		printf("Digite o valor da nota\n");
		scanf("%f", &valor1);
		printf("Digite o valor da 2° nota\n");
		scanf("%f", &valor2);
		printf("Digite o valor da 3° nota\n"); 
		scanf ("%f", &valor3); 
		
		media = (valor1 + valor2 + valor3)/3;
		
		printf("A media das notas e: %f", media);
		
	system ("pause");
		
	}
	
		
