#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //TODO ask user for height
    int altura, fila, columna, espacio;

    do

    {

        altura = get_int("Enter desired height between 1 and 8\n");

    }

    while (altura < 1 || altura > 8);

    // Setting loops so rows and height are equal

    for (fila = 0; fila < altura; fila++)

    {

        // Calculating how many spaces

        for (espacio = 0; espacio < altura - fila - 1; espacio++)

        {

            printf(" ");

        }

        // Calulating how many #

        for (columna = 0; columna <= fila; columna++)

        {

            printf("#");

        }

        printf("\n");

    }

}