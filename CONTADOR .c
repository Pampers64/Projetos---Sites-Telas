#include<stdio.h>
#include<stdlib.h>

	int main ()
	{
		int contador, Mn=0 , i; 
		
		for (i = 0; i <=10; i++)
		{
			printf("Digite um valor:\n");
			
			scanf ("%d", &contador);
		
			if(contador > Mn)
			
			{
				Mn = contador;
			}
			
			printf("O maior numero e: %d\n", Mn);
	    }
		system ("PAUSE");
		
	}
