// Practice writing a function to find a max value

#include <cs50.h>
#include <stdio.h>

int max(int array[], int n);

int main(void)
{
    int n;
    do
    {
        n = get_int("Number of elements: ");
    }
    while (n < 1);

    int array[n];

    for (int i = 0; i < n; i++)
    {
        array[i] = get_int("Element %i: ", i);
    }

    printf("The max value is %i.\n", max(array, n));
}

// TODO: return the max value
int max(int array[], int n)
{
    // starting with max with the first number
    int max = array[0];
    // i = 1 because max started already with first number (but it works with 0 anyway)
    for (int i = 1; i < n; i++)
    {
        // here im checking if the current [i] number in the array is bigger than "max" and updating it if so
        if (array[i] > max)
        {
            max = array[i];
        }
    }
return max;

}
