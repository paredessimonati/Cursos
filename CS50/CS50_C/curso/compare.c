#include <stdio.h>
#include <cs50.h>

int main (void)
{
   int x = get_int("what's x? ");
   int y = get_int("What's y? ");

   if (x < y)
   {
    printf("x is less than y\n");
   }
   else if (x > y)
   {
    printf("x is not less than y\n");
   }
   else
   {
    printf("son iguales las weás\n");
   }
}