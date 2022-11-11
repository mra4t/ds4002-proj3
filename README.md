# Can We Judge A Movie By Its Poster?

## SRC
### Installing / Building the Code
To install any of the code files, download the flile from the SRC folder.

#### R Markdown Files (.Rmd)
To run the R Markdown files, open the file in RStudio and execute.  All of the necessary libraries are listed at the top of the file, so you can install them if you do not already have them, and then run the file to build the code.

#### Python Files (.py)
To run the Python files, you can either open the file in your preferred IDE and run the code, or you can execute on the command line using "python3 <filename.py>".  The required packages are listed at the top of the file, so you can install them if you do not already have them, and then run the file to build the code.  Note that these files produce a Microsoft Excel Sheet in the directory in which you download them.

### Code Usage
This code makes use of a Decision Tree Model to determine which components/attributes of a movie poster contribute to the movie's success. 

## DATA
Our data was obtained from Kaggle [here](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows).

### Data Dictionary
| Column  | Description | Potential Values |
| ------ |  ----------- | ----------------
| Poster_Link  | A URL pointing to the image of the official movie poster | A string of the image URL |
| Series_Title | The title of the movie | A string of texts with <= 280 characters |
| Gross | The total revenue earned by that movie | Integer value from 1,300 to 937,000,000 |
| IMDB_Rating | The rating of the movie on IMDB | Integer value from 7.6 to 9.3 |
| Released_Year | The year that the movie was released | A string containing numerical values from the year  1920 to 2020 |
| Genre | The genres that the movie belongs to | A string containing different combinations of genres with no more than 4 different genres per movie |
| Whitespace_Rate | The percentage of pixels in the image that are white | Integer value from 0 to 1 |
| face | | |
| color | | |

## FIGURES
| Figure Number | Figure Name | Key Takeaways |
| ----------- | ------ |  ----------- |
Figure 1 | figure title | key takeaways

## REFERENCES
[Milestone 1: Creating a Hypothesis](https://docs.google.com/document/d/1fQZCOykrO4nFIoZqL5Ej57IBHdYpFPkob-57JDN4Rl0/edit?usp=sharing)

[Milestone 2: Exploratory Data Analysis & Analysis Plan](https://docs.google.com/document/d/1E2CEzyIloxH_UvfVl4ng98CzRZ7kH1L3C6sKljVKMv0/edit?usp=sharing)

[1] K. Osburn, “Top 10 U.S. Hobbies,” eHow, 31-Jan-2018. [Online]. Available: https://www.ehow.com/slideshow_12221978_top-us-hobbies.html. [Accessed: 02-Nov-2022].

[2] Statista, “TV, Video &amp; Film,” Statista. [Online]. Available: https://www.statista.com/markets/417/topic/476/tv-video-film/#overview. [Accessed: 02-Nov-2022]. 

[3] J. G. Navarro, “U.S. & Canada: Movie releases per year 2021,” Statista, 10-Mar-2022. [Online]. Available: https://www.statista.com/statistics/187122/movie-releases-in-north-america-since-2001/. [Accessed: 02-Nov-2022]. 

[4] Chilliprinting, “How to use color psychology to trigger emotions with posters,” Chilliprinting Blog, 11-May-2021. [Online]. Available: https://www.chilliprinting.com/Online-Printing-Blog/use-color-psychology-emotions-poster/. [Accessed: 02-Nov-2022]. 

[5] H. Shankhdhar, “IMDB movies dataset,” Kaggle, 01-Feb-2021. [Online]. Available: https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows. [Accessed: 02-Nov-2022]. 

[6] “Find most used colors in image using Python,” GeeksforGeeks, 16-Oct-2021. [Online]. Available: https://www.geeksforgeeks.org/find-most-used-colors-in-image-using-python/. [Accessed: 02-Nov-2022]. 
