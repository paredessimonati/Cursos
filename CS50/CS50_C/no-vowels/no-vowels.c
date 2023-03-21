// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(int argc, string argv[])
{

    string replace = argv[1];
    for (int i = 0; i < strlen(replace); i++)
    {
        if (replace[i] == 'a')
        {
            printf("6");
        }
        else if (replace[i] == 'e')
        {
            printf("3");
        }
        else if (replace[i] == 'i')
        {
            printf("1");
        }
        else if (replace[i] == 'o')
        {
            printf("0");
        }
        else
        {
            printf("%c", replace[i]);
        }


    }

    printf("\n");

}

