#include <stdio.h>
#include <stdlib.h>

	int main() 
	{
		
		int num;
		//entrada
		printf("Digite o número desejado\n");
		scanf("%d", &num);
		
		//processamento
		 
		if(num == 0)
		
		{
		
			printf("O numero informado eh igual a zero\n");
		}
		else
		{
				
			
			if(num > 0)
			
			{
				
			printf ("O numero informado eh maior que zero\n");
			
			}
			
			else
			
			{	  		
			
				printf ("O numero informado eh menor que zero\n");
				
			}
	}
}
