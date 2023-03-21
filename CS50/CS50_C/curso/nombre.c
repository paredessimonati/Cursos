#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string nombre = get_string("What's your first name? ");
    string apellido = get_string("What's your last name? ");
    printf("hello, %s %s\n", nombre, apellido);
}