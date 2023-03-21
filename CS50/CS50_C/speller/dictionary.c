// Implements a dictionary's functionality
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <stdbool.h>
#include <strings.h>
#include <string.h>
#include <math.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 10000;

// Hash table
node *table[N];
int hash_value = 0;
int word_count = 0;

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // Hash the word to obtain value
    int index = hash(word);
    // Access linked list at that index in the hash table
    node *cursor = table[index];
    // Traverse linked list, looking for the word (strcasecmp)
    while (cursor != NULL)
    {
        if (strcasecmp(word, cursor->word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // Adds first letter as index
    hash_value = toupper(word[0]) - 'A';
    // Adds second character index, if there's no 2nd letter or ', ends the hash
    if (isalpha(word[1]))
    {
        hash_value += toupper(word[1]) - 'A';
    }
    else if (word[1] == '\'')
    {
        hash_value += 27;
    }
    return hash_value;
    /*  If someone ever comes here to check.. i tried to do something more
        fun using pow and modulus and stuff like that.. but it was really
        really slow.. like 7 seconds slow, when i removed it and left just the
        2 word[n] checks it took like .4 seconds. the value of N for the table
        did no noticeable difference... tried with n = 10 to n = 200000, always
        the same
     */
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open Dictionary file
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        printf("Unable to load Dictionary\n");
        return false;
    }
    // Read Strings from file one at a time
    char tmp[LENGTH + 1];
    while (fscanf(dict, "%s", tmp) != EOF)
    {
        // Create a New node for each word
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return false;
        }
        // Copy word
        strcpy(n->word, tmp);
        // Hash word to obtain a hash value
        int pos = hash(tmp);
        // insert node into hash table at that location
        n->next = table[pos];
        table[pos] = n;
        word_count++;


    }

    fclose(dict);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{

    return word_count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *cursor = table[i];
        while (cursor != NULL)
        {
            node *oscar = cursor->next;
            free(cursor);
            cursor = oscar;
        }
    }

    return true;
}
