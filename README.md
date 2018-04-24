# Data Science Portfolio

Here we have a growing collection of work I've done in the area of data science. The first works that will be loaded here are focused on data cleaning and visualization rather than machine learning. I'm on [LinkedIn](https://www.linkedin.com/in/akdcm/) and [Twitter](https://twitter.com/kaumaron). Here's my [resume](https://www.dropbox.com/s/tbdrmbaexzqk6v5/Andrew%20DeCotiis-Mauro%20Data%20Scientist%20-%2003222018.pdf?dl=0).

## CEO Compensation Analysis
I've completed an analysis of [CEO Compensation](https://github.com/kaumaron/Data_Science/blob/master/CEO_Compensation/CEO_Compensation.ipynb). The project was motivated by a Wall Street Journal article about female CEOs having a higher median pay. I have a write up of the project that is less detailed in [Towards Data Science](https://towardsdatascience.com/female-ceos-have-a-higher-median-pay-but-is-it-related-to-their-gender-40d0662b7d4f) on Medium's network of publications.

<img src="https://cdn-images-1.medium.com/max/800/1*eIP6lGLKWgfzj-nn2Zkqwg.png" width="100%"/>

## Congressional Partisanship
As a study in visualization with `matplotlib` and `seaborn`, I scraped data from the Senate and House websites that listed the members of each Congress and how many seats each party had. The results are written up in the [Senate Partisanship](https://github.com/kaumaron/Data_Science/blob/master/Congressional_Partisanship/Senate%20Partisanship.ipynb) Jupyter notebook. There is a short write up of the results on [Towards Data Science](https://towardsdatascience.com/congressional-partisanship-a-visualization-c7bc448fd3e). You can directly view the [Tableau visualization here](https://public.tableau.com/views/CongressionalPartisanship/Dashboard1?:embed=true&:display_count=no). 

<iframe src="https://public.tableau.com/views/CongressionalPartisanship/Dashboard1?:showVizHome=no&:embed=true" width="100%" height="500"></iframe>

## Twitter Bots
I've created a couple of Twitter bots that retweet (RT) specific types of tweets. I have a bot that RTs data science and artificial intelligence news ([@akdm_bot](https://twitter.com/akdm_bot), currently at just over 650 followers). I also created a bot for a friend's alternative history podcast ([@what_if_history](https://twitter.com/what_if_history)). The bot helped increase his audience engagement and helped to bring the number of followers from between 20 and 40 to around 1150. Both bots are toy projects at the moment and have kinks that need to be worked out. The code is available in my [Twitter Bots repository](https://github.com/kaumaron/TwitterBots).

## Technical Writing
I'm a person who enjoys writing and editing. I've been working with Towards Data Science since early January 2018 as an editorial associate. The position entails approving posts on Medium and providing constructive feedback to writers. I became a writer for TDS in early December. Since then I've been continuing to write. Some selected posts include:
* [Fighting Cancer with Artificial Intelligence: Part 0 — Deep Learning](https://towardsdatascience.com/fighting-cancer-with-artificial-intelligencepart-0-deep-learning-a6f0b375c8c)
* [Congressional Partisanship: A Visualization](https://towardsdatascience.com/congressional-partisanship-a-visualization-c7bc448fd3e)
* [Female CEOs Have a Higher Median Pay, But Is It Related to Their Gender?](https://towardsdatascience.com/female-ceos-have-a-higher-median-pay-but-is-it-related-to-their-gender-40d0662b7d4f)
* [What’s the Use of All This Data If No One Wants to Look at It?](https://medium.com/@akdm/whats-the-use-of-all-this-data-if-no-one-wants-to-look-at-it-a64f56d113c2)

## Tableau Visualizations
Here is a list of [my public](https://public.tableau.com/profile/andrew.k.decotiis.mauro#!/) Tableau visualizations:
* [Endangered World Languages](https://public.tableau.com/profile/andrew.k.decotiis.mauro#!/vizhome/EndangeredWorldLanguages/Dashboard1)
* [Congressional Partisanship](https://public.tableau.com/profile/andrew.k.decotiis.mauro#!/vizhome/CongressionalPartisanship/Dashboard1)
* [News Source Biases Summary](https://public.tableau.com/profile/andrew.k.decotiis.mauro#!/vizhome/NewsSourceBiases/AverageNewsSourceBias) and [Breakdown](https://public.tableau.com/profile/andrew.k.decotiis.mauro#!/vizhome/NewsSourceBiases-FactualContentRating/NewsSourceBias)
* [Student Growth - Grade 1 - Math](https://public.tableau.com/profile/andrew.k.decotiis.mauro#!/vizhome/Grade1MathStudentGrowth-SABronx1/Dashboard1)
* [Where MSDA Grads Go to College](https://public.tableau.com/profile/andrew.k.decotiis.mauro#!/vizhome/WhereMSDAGradsGoToCollege/MSDAGraduatesSchools)


## Packt Publishing Free-Learning E-Books
[Packt Publishing](https://www.packtpub.com/) has a daily e-book that is offered for free as long as you sign-up for an account and visit the [Free Learning](https://www.packtpub.com/packt/offers/free-learning) page. As part of my morning routine, I check my email, so I wrote [a scraper](https://github.com/kaumaron/Data_Science/tree/master/FreeLearning) that gathers the title of the book and a description and sends an email to a list of users. I have three versions: `Free_Book_Scraper.py` is the first version that I wrote with an HTML email, `Free_Book_Scraper_HTML_color.py` is an newer version that included an HTML button with a button that changed color to match the colors of the book,  `Free_Book_Scraper_html_w_colors.py` is the current version that I run on my AWS EC2 instance (if you are interested in joining that list send an [email](mailto:andrewkmauro@gmail.com?subject=Packt%20Free%20Learning&body=Please%20add%20me%20to%20the%20list)).

## Grade Analysis
As part of an interview for an administrative position at a charter school, I took a look at some sample grade data from a Math Test that was taken in September and December and analyzed the results. The [write up](https://github.com/kaumaron/Data_Science/blob/master/Grade_Analysis/Student%20Achievement.ipynb) is anonymized to obscure the names and classes of the students in the sample data set.

## Graduate Map
In order to allow future and current families at my current school explore which colleges and regions of the coutry graduates go to, I created an interactive map that includes the colleges and majors of graudates from 2009 to 2017. The [Tableau visualization can be viewed directly here](https://public.tableau.com/profile/andrew.k.decotiis.mauro#!/vizhome/WhereMSDAGradsGoToCollege/MSDAGraduatesSchools).

<iframe src="https://public.tableau.com/views/WhereMSDAGradsGoToCollege/MSDAGraduatesSchools?:showVizHome=no&:embed=true" width="100%" height="500"></iframe>
