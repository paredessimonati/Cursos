#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // Get imput from the user
    string word;
    word = get_string("Please enter message to be displayed in binary: ");

    // convert binary

    for (int i = 0, len = strlen(word); i < len; i++)
    {
        int character = word[i];
        int array[8];

        // going up the numbers converting them and storing the 1s and 0s in the array array (i know i know)
        for (int a = 0; a < 7; a++)
        {
            if (character % 2 != 0)
            {
                array[a] = 1;
            }
            else
            {
                array[a] = 0;
            }
            character /= 2;
        }

        // printing the array backwards so i get the correct order for the bulbs
        for (int b = 7; b >= 0; b--)
        {
            print_bulb(array[b]);
        }

        printf("\n");
    }
}



void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
