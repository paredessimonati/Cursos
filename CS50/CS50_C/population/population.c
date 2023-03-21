#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // Prompt for start size
    int start_size;
    do
    {
        start_size = get_int("What's the initial llama population? (Has to be greater than 9)\n");
    }
    while (start_size < 9);


    // TODO: Prompt for end size
    int end_size;
    do
    {
        end_size = get_int("What's the desired end population? (Has to be greater than starting population)\n");
    }
    while (end_size<start_size);


    // TODO: Calculate number of years until we reach threshold
    int years = 0;

    while (start_size < end_size)
    {
        start_size = start_size + start_size/3 - start_size/4;
        years++;
    }



    // TODO: Print number of years

    printf("Years: %i\n", years);
}
