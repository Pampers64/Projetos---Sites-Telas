#include <stdio.h>

int main() {
	
	int num = 0;
	int soma = 0;
	
	printf("Insira um numero natural positivo: ");
	scanf("%d", &num);
	
	for (int i = 1; i <= num; i++) {
		
		soma += i;
		
	}
	
	printf("Soma: %d", soma);
	
}
