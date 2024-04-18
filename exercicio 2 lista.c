#include <stdio.h>

int main() {
    float fulanoaltura = 1.50, ciclanoaltura = 1.10;
    int anos = 0;

    while (ciclanoaltura <= fulanoaltura)
	 {
        fulanoaltura += 0.02;  
        ciclanoaltura += 0.03;  
        anos++;
    }

    printf("Serão necessários %d anos para que Ciclano seja mais alto que Fulano.\n", anos);

    return 0;
}
