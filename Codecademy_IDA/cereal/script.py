from __future__ import division
#import codecademylib
import numpy as np

#import calorie information
calorie_stats = np.genfromtxt('cereal.csv',
                              delimiter = ',')

#Find average calories in dataset
average_calories = np.mean(calorie_stats)
print('Average Calories in Cereal: {}'.format(
		average_calories))

#sort calores to see distribution
calorie_stats_sorted = sorted(calorie_stats)
print('Sorted Calorie Stats:\n{}'.format(
			calorie_stats_sorted))

#Find median of dataset
median_calories = np.median(calorie_stats)
print('\nMedian calories: {} cal'.\
      format(median_calories))

#Determine first percentile greater than 60 calories
nth_percentile = 0
for i in range(100):
  if np.percentile(calorie_stats, i) > 60:
    nth_percentile = i
    break
print('\nFirst percentile above 60 cal: {}%'.\
      format(nth_percentile))

#Determine percentage of cereals with calories greater than 60
more_calories = len([x for x in calorie_stats \
                     if x > 60]) / \
		    calorie_stats.shape[0] * 100
print('\nPercent of cereals with greater' \
      ' than 60 calories: {:.2f}%'.\
      format(more_calories))

#Determine the standard deviation for the dataset
calorie_std = np.std(calorie_stats)
print('\nThe standard deviation of calories: {:.2f}'.\
     format(calorie_std))

# CrunchieMunchies has 60 calories per serving.
# Compared to the competition, it's much healthier.
# 97% of competitor's cereals have more calories
# and the median calories in a serving of cereal
# is 110 calories -- a full 83% more!
