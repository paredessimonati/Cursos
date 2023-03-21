#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    float index = 0;
    int decimal = 0;
// get text from user
    string text = get_string("Text: ");

// doing the Coleman-Liau algorithm (i had to add float to every variable for it to work, adding .0 to 100 wasnt enough to convert the whole thing to a float)
    float L = ((float)count_letters(text) / (float)count_words(text) * 100.0);
    float S = ((float)count_sentences(text) / (float)count_words(text) * 100.0);
    index = (0.0588 * L - 0.296 * S - 15.8);
    index = roundf(index);

// converting the index to integer
    decimal = (int)index;

    // printf("%d\n", decimal);

    if (decimal >= 1 && decimal < 16)
    {
        printf("Grade %d\n", decimal);
    }
    else if (decimal > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Before Grade 1\n");
    }
    // printf("%d letters\n%d words\n%d sentences\n", count_letters(text), count_words(text), count_sentences(text));
}

// counting letters

int count_letters(string text)
{
    int letters = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isalpha(text[i]))
        {
            letters += 1;
        }
    }
    return letters;
}

// counting words

int count_words(string text)
{
    int words = 1;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (isspace(text[i]))
        {
            words += 1;
        }
    }
    return words;

}

// counting sentences

int count_sentences(string text)
{
    int sentences = 0;
    for (int i = 0, len = strlen(text); i < len; i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentences += 1;
        }
    }
    return sentences;
}