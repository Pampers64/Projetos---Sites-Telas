#include <stdio.h>

int retornaFatorial(int numero) {
	
	int fatorial = 1;
	
	for(int i = 1; i <= numero; i++) {
		
		fatorial *= i;
		
	}
	return fatorial;	
}

int main() {
	
	float soma = 1;
	float N = 0;
	
	printf("Digite um numero inteiro e positivo: ");
	scanf("%f", &N);
	
	for(int i = 1; i <= N; i++) {
		
		soma += (1.0/retornaFatorial(i));
	}
	
	printf("%f", soma);
}
