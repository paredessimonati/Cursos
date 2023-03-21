#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //TODO ask user for height
    int h, i, k, j;

    do

    {

        h = get_int("Enter desired height between 1 and 8\n");

    }

    while (h < 1 || h > 8);

    // Setting loops so rows and height are equal

    for (i = 0; i < h; i++)
    {
        // Calculating how many spaces
        for (j = 0; j < h - i - 1; j++){
            printf(" ");
        }

        // Calulating how many #
        for (k = 0; k <= i; k++){
            printf("#");
        }
        printf("  ");

        for (k = 0; k <= i; k++){
            printf("#");
        }
        printf("\n");

    }
}