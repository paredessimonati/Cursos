#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


#define BLOCK_SIZE 512
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // Checks for proper syntax
    if (argc != 2)
    {
        printf("Usage: recover filename.raw\n");
        return 1;
    }

    // Open input file and checks if its possible to open
    FILE *raw_file = fopen(argv[1], "r");
    if (raw_file == NULL)
    {
        printf("Could not open %s.\n", argv[1]);
        return 1;
    }

    // setting up a counter to name the files
    int count = 0;
    BYTE buffer[BLOCK_SIZE];
    char filename[8];
    // initializing 'filename' with 000.jpg so fopen in the else loop has something to append to
    sprintf(filename, "%03i.jpg", count);

    //  main thing, reading the raw file in chunks of 512 bytes
    while (fread(buffer, 1, BLOCK_SIZE, raw_file) == BLOCK_SIZE)
    {
        // checking for jpg header for a new jpg file
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // creating a new jpg file and updating count
            sprintf(filename, "%03i.jpg", count);
            count++;
            FILE *jpg = fopen(filename, "w");

            // writing the buffer to the 'filename' file
            fwrite(buffer, 1, BLOCK_SIZE, jpg);
            fclose(jpg);

        }
        // if no new file is found in the raw data, then it appends what is in the buffer to the already created file
        else
        {
            FILE *jpg = fopen(filename, "a");
            fwrite(buffer, 1, BLOCK_SIZE, jpg);
            fclose(jpg);
        }

    }
    //closing original file
    fclose(raw_file);
}
