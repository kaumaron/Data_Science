# Data Science Portfolio

Here we have a growing collection of work I've done in the area of data science. The first works that will be loaded here are focused on data cleaning and visualization rather than machine learning.

## CEO Compensation Analysis
I've completed an analysis of [CEO Compensation](https://github.com/kaumaron/Data_Science/blob/master/Congressional_Partisanship/Senate%20Partisanship.ipynb). The project was motivated by a Wall Street Journal article about female CEOs having a higher median pay. I have a write up of the project that is less detailed in [Towards Data Science](https://towardsdatascience.com/female-ceos-have-a-higher-median-pay-but-is-it-related-to-their-gender-40d0662b7d4f) on Medium's network of publications.

## Packt Publishing Free-Learning E-Books
[Packt Publishing](https://www.packtpub.com/) has a daily e-book that is offered for free as long as you sign-up for an account and visit the [Free Learning](https://www.packtpub.com/packt/offers/free-learning) page. As part of my morning routine, I check my email, so I wrote [a scraper](https://github.com/kaumaron/Data_Science/tree/master/FreeLearning) that gathers the title of the book and a description and sends an email to a list of users. I have three versions: `Free_Book_Scraper.py` is the first version that I wrote with an HTML email, `Free_Book_Scraper_HTML_color.py` is an newer version that included an HTML button with a button that changed color to match the colors of the book,  `Free_Book_Scraper_html_w_colors.py` is the current version that I run on my AWS EC2 instance (if you are interested in joining that list send an [email](mailto:andrewkmauro@gmail.com?subject=Packt%20Free%20Learning)).

## Grade Analysis
As part of an interview for an administrative position at a charter school, I took a look at some sample grade data from a Math Test that was taken in September and December and analyzed the results. The [write up](https://github.com/kaumaron/Data_Science/blob/master/Grade_Analysis/Student%20Achievement.ipynb) is anonymized to obscure the names and classes of the students in the sample data set.

## Congressional Partisanship
As a study in visualization with `matplotlib` and `seaborn`, I scraped data from the Senate and House websites that listed the members of each Congress and how many seats each party had. The results are written up in the [Senate Partisanship](https://github.com/kaumaron/Data_Science/blob/master/Congressional_Partisanship/Senate%20Partisanship.ipynb) Jupyter notebook. I plan on writing a short Medium piece as well. 
