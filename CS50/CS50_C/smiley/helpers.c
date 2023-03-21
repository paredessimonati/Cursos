#include "helpers.h"

void colorize(int height, int width, RGBTRIPLE image[height][width])
{
    // For loops to go through each pixel
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // If the pixel is black (0,0,0) then....
            if (image[i][j].rgbtRed == 0 && image[i][j].rgbtGreen == 0 && image[i][j].rgbtBlue == 0)
            {
                // Use values from 0 to 255 to change the color
                // 255,0,255 is a nice calm MAGENTA
                image[i][j].rgbtRed = 255;
                image[i][j].rgbtGreen = 0;
                image[i][j].rgbtBlue = 255;
            }
        }
    }

}
