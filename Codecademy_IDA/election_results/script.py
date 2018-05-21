#import codecademylib
from __future__ import division
import numpy as np
import matplotlib
matplotlib.use('qt5agg')
import matplotlib.pyplot as plt

survey_responses = np.array(
                    ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos',
                    'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos',
                    'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan',
                    'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan',
                    'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan',
                    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan',
                    'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
                    'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan',
                    'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan',
                    'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan',
                    'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan',
                    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan',
                    'Kerrigan', 'Ceballos', 'Kerrigan', 'Kerrigan',
                    'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan',
                    'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan',
                    'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan',
                    'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan',
                    'Kerrigan', 'Ceballos']
                    )

# Determine total votes for Ceballos
total_ceballos = np.sum(survey_responses == 'Ceballos')
print('Total votes for Ceballos: {}'.format(
  total_ceballos))

# Determine Percentage of votes for Ceballos
percentage_ceballos = total_ceballos * 100 / survey_responses.size
print('Percentage of Vote for Ceballos: {:.2f}%'.format(
  percentage_ceballos))

# Create Binomal Distribution for survey with n = 70
possible_surveys = np.random.binomial( 70, percentage_ceballos / 100,
    size = 10000) / 70.
plt.hist(possible_surveys, range = (0,1), bins = 20)
plt.show()


# Determine how many surveys show results under 50%
ceballos_loss_surveys = np.sum(possible_surveys < 0.50) /\
    possible_surveys.size * 100
print('Percent of binomial distributed survey results' +
         ' under 50%: {:.2f}%'.format(
         ceballos_loss_surveys))

# Create distribution for larger survey
large_survey = np.random.binomial( 7000, percentage_ceballos / 100,
    size = 10000) / 7000.

# Determine percent of surveys under 50% with new distribution
ceballos_loss_new = np.sum(large_survey < 0.50) / large_survey.size * 100
print('Percent of large binomial distributed survey results' +
     ' under 50%: {:.2f}%'.format(
     ceballos_loss_new))
