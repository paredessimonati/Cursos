#include "helpers.h"
#include "math.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //Going through each pixel to convert them to grayscale by averaging
            //the values in .rgbtRed Green and Blue and writing the result back.
            int gray = round((image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue) / 3.0);
            image[i][j].rgbtRed = gray;
            image[i][j].rgbtGreen = gray;
            image[i][j].rgbtBlue = gray;
        }

    }

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Defining variables for the algorithm
            int originalRed = image[i][j].rgbtRed;
            int originalGreen = image[i][j].rgbtGreen;
            int originalBlue = image[i][j].rgbtBlue;
            // algorithm
            int sepiaRed = round(.393 * originalRed + .769 * originalGreen + .189 * originalBlue);
            int sepiaGreen = round(.349 * originalRed + .686 * originalGreen + .168 * originalBlue);
            int sepiaBlue = round(.272 * originalRed + .534 * originalGreen + .131 * originalBlue);
            // capping values to 255
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }
            // writing new values
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }

    }

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        // width needs to be halved because as you swap pixels if you go past the half you start putting
        // them in order again
        for (int j = 0; j < width / 2; j++)
        {
            // Goes to each pixel and swaps it for the pixel at the other side using j and (width - j)
            int x = j;
            int y = (width - j - 1);
            // tmp has to use the RGBTRIPLE struct to hold the values for the three colors
            RGBTRIPLE tmp = image[i][x];
            image[i][x] = image[i][y];
            image[i][y] = tmp;

        }

    }

    return;
}


// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // making a copy of the image to use it to calculate pixel value
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // copying values from "image" to "copy"
            copy[i][j] = image[i][j];
        }
    }
    // second loop, for every pixel of the image
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //getting some variables ready for later
            int sumRed = 0;
            int sumGreen = 0;
            int sumBlue = 0;
            float div = 9.0;
            RGBTRIPLE tmp;

            // this loop iterates over a 3x3 square surrounding the current pixel of the second loop
            for (int k = 0; k < 3; k++)
            {
                for (int l = 0; l < 3; l++)
                {
                    // making some variables to neat things up
                    int a = (i + k - 1);
                    int b = (j + l - 1);

                    // checking if the pixel in the 3x3 area is outside or inside the image
                    if ((a >= 0) && (a < height) && (b >= 0) && (b < width))
                    {
                        //adding up the values of red green and blue.
                        sumRed += copy[a][b].rgbtRed;
                        sumGreen += copy[a][b].rgbtGreen;
                        sumBlue += copy[a][b].rgbtBlue;
                    }
                    else
                    {
                        //if pixel is outside the image, reduces the divisor by 1 (since there will be fewers pixels)
                        div--;
                    }

                }
            }
            // getting the averages
            tmp.rgbtRed = round(sumRed / div);
            tmp.rgbtGreen = round(sumGreen / div);
            tmp.rgbtBlue = round(sumBlue / div);

            // assign calculated values from "copy" to "image"
            image[i][j] = tmp;
        }
    }
    return;
}
