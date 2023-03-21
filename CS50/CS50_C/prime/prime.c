#include <cs50.h>
#include <stdio.h>

bool prime(int number);

int main(void)
{
    int min;
    do

    {
        min = get_int("Minimum: ");
    }

    while (min < 1);

    int max;
    do

    {
        max = get_int("Maximum: ");
    }

    while (min >= max);

    for (int i = min; i <= max; i++)

    {
        if (prime(i))
        {
            printf("%i\n", i);
        }
    }
}

bool prime(int number)

{
    if (number <= 1) return false;  // 0 and 1 are not considered prime numbers

    for (int i = 2; i < number; i++) {
        if (number % i == 0) return false;  // n is divisible by i, so it is not prime
    }

    return true;  // n is not divisible by any number from 2 to n-1, so it is prime
}