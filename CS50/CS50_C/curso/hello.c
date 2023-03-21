#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // Setting up string variables
    string name;

    name = get_string("What's your name? \n");

    {

        // printing the variable name
        printf("Hello %s\n", name);

    }

}