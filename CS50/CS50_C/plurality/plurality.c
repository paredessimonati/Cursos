#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    //get "name" of the candidate voted for
    for (int i = 0; i < candidate_count; i++)
    {
        //if name matches
        //originally i didnt want to use the strcmp function, i tried using if(name == candidates[i].name) to keep it simple but that didnt work, i couldnt use
        //debug50 to check why
        if (strcmp(name, candidates[i].name) == 0)
        {
            //candidate++ and "return true"
            candidates[i].votes++;
            return true;
        }

    }

    // TODO
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    int win = 0;
    // searching for most votes
    for (int i = 1; i < candidate_count; i++)
    {
        if (candidates[i].votes > candidates[win].votes)
        {
            win = i;
        }
    }
    // here i wanted to print the winner and then do a for loop to check if there was any ties
    //printf("Winner is %s with %d votes\n", candidates[win].name, candidates[win].votes);
    for (int i = 0; i < candidate_count; i++)
    {
        // this printed the winner AND anyone tied, so i left this instead.
        if (candidates[i].votes == candidates[win].votes)
        {
            printf("%s\n", candidates[i].name);
        }
    }
    return;
}