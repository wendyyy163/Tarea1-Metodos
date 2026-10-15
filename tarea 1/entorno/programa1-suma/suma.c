#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    double x, y;

    // Si se pasan números directamente en la terminal, los usa
    if (argc >= 3) {
        x = atof(argv[1]);
        y = atof(argv[2]);
    } else {
        // Si no se pasaron números, los pide de forma interactiva
        printf("Ingrese el numero 1: ");
        if (scanf("%lf", &x) != 1) x = 0.1;
        
        printf("Ingrese el numero 2: ");
        if (scanf("%lf", &y) != 1) y = 0.2;
    }

    double resultado = x + y;
    printf("%.17g\n", resultado);
    return 0;
}