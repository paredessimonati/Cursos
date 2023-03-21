// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);
    // Make an array name header to store the data from the input file using the HEADER_SIZE constant
    uint8_t header[HEADER_SIZE];
    // Read the 44 bytes header of the input file
    fread(header, HEADER_SIZE, 1, input);
    // Writes the same data read from input file and sends it to output file
    fwrite(header, HEADER_SIZE, 1, output);

    // Start a buffer of 16 bites (2 bytes) because sample size in output is 2 bytes
    int16_t buffer;
    // Loop that reads 1 sample of size 2 from input file and stores the value in at the location of buffer
    while (fread(&buffer, 2, 1, input))
    {
        // multiplies the buffer by the factor
        buffer *= factor;
        // same as before, writes the data from buffer to the output file
        fwrite(&buffer, 2, 1, output);
    }

    // Close files
    fclose(input);
    fclose(output);
}
