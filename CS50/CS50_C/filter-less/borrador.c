void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // making a copy of the image to use it to calculate pixel value
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int sumRed = 0;
            int sumGreen = 0;
            int sumBlue = 0;
            float div = 9.0;
            RGBTRIPLE tmp;

            for (int k = 0; k < 2; k++)
            {
                for (int l = 0; l < 2; l++)
                {
                    int a = (i + k - 1);
                    int b = (j + l - 1);
                    if ((a < 0) || (a > height))
                    {
                        a = 0;
                        div--;
                    }

                    if ((b < 0) || (b > width))
                    {
                        b = 0;
                        div--;
                    }

                    sumRed += copy[a][b].rgbtRed;
                    sumGreen += copy[a][b].rgbtGreen;
                    sumBlue += copy[a][b].rgbtBlue;
                }
            }

            tmp.rgbtRed = round(sumRed / div);
            tmp.rgbtGreen = round(sumGreen / div);
            tmp.rgbtBlue = round(sumBlue / div);

            image[i][j] = tmp;
        }
    }
    return;
}