#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long tarjeta;

    // get credit card number
    tarjeta = get_long("Please insert your credit card number: \n");

    //divide by ten and count to get number of digits
    int digito = 0;
    long numero = tarjeta;
    while (numero > 0)
    {
        numero = numero / 10;
        digito++;
    }

    // if digits are outside parameters print error message
    if (digito != 13 && digito != 15 && digito != 16)
    {
        printf("INVALID\n");
        return 0;
    }

    //luhn's algorithm
    int suma1 = 0, suma2 = 0, total = 0, digito1, digito2, modulo1, modulo2;
    long numero2 = tarjeta;

    do
    {
        //removing last digit and adding mod1
        modulo1 = numero2 % 10;
        numero2 = numero2 / 10;
        suma1 = suma1 + modulo1;
        //remove second digit and adding mod2*2
        modulo2 = numero2 % 10;
        numero2 = numero2 / 10;
        modulo2 = modulo2 * 2;
        digito1 = modulo2 % 10;
        digito2 = modulo2 / 10;
        suma2 = suma2 + digito1 + digito2;
    }
    while (numero2 > 0);
    total = suma1 + suma2;

    if (total % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }

    // verifying cards

    long primeros_numeros = tarjeta;

    do
    {
        primeros_numeros = primeros_numeros / 10;
    }
    while (primeros_numeros > 100);

    if (primeros_numeros >= 51 && primeros_numeros <= 55)
    {
        printf("MASTERCARD\n");
    }
    else if (primeros_numeros == 34 || primeros_numeros == 37)
    {
        printf("AMEX\n");
    }
    else if (primeros_numeros >= 40 && primeros_numeros <= 49)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }



    //borrar antes de terminar
    //long prueba = (tarjeta / 10);


    //printf("%ld\n", primeros_numeros);
    //printf("%d\n", digito);
    //printf("%ld \n", corto);
}




    for i in range(digit-2, -1, -2):
        double = int(card[i]) * 2
        for digit in str(double):
            sum1 += int(digit)
        sum1 += int(card[i + 1])
    return sum1 % 10 == 0


