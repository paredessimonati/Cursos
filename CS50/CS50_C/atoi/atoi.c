#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int convert(string input);

int main(void)
{
    string input = get_string("Enter a positive integer: ");

    for (int i = 0, n = strlen(input); i < n; i++)
    {
        if (!isdigit(input[i]))
        {
            printf("Invalid Input!\n");
            return 1;
        }
    }

    // Convert string to int
    printf("%i\n", convert(input));
}

int convert(string input)
{
    // Base case
    if (strlen(input) == 0)
    {
        return 0;
    }

    // Get the last char in the string
    int lastIndex = strlen(input) - 1;
    char lastChar = input[lastIndex];
    // Convert char to int
    int lastInt = lastChar - 48;
    // Remove the last char from the string
    input[lastIndex] = '\0';
    // Recursive call
    return lastInt + 10 * convert(input);
}