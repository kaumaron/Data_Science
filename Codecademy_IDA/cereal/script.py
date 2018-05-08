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
def per_find(method):
    nth_percentile = 0
    for i in np.linspace(0,100, num = 1000000):
        if np.percentile(calorie_stats, i, interpolation = method) > 60:
            nth_percentile = i
            return nth_percentile

# Exploring the effect of percentile interpolation on result
percentiles = []
for i in ['linear', 'lower', 'higher', 'midpoint', 'nearest']:
   percentiles.append((i,per_find(i)))
print('\nFirst percentile above 60 cal:')
for k,v in percentiles:
    print('{}: {}'.format(k,v))

#Determine percentage of cereals with calories greater than 60
more_calories = len([x for x in calorie_stats \
                     if x > 60]) / \
		    calorie_stats.shape[0] * 100
print('\nPercent of cereals with greater' \
      ' than 60 calories: {:.2f}%'.\
      format(more_calories))

# Determining closest sum to 100 for percentile + percent cals
print('Percentile + Percent Over 60 Cal:')
for k,v in percentiles:
    print('{}: {:.6f}'.format(k,v+more_calories))

#Determine the standard deviation for the dataset
calorie_std = np.std(calorie_stats)
print('\nThe standard deviation of calories: {:.2f}'.\
     format(calorie_std))

# CrunchieMunchies has 60 calories per serving.
# Compared to the competition, it's much healthier.
# 97% of competitor's cereals have more calories
# and the median calories in a serving of cereal
# is 110 calories -- a full 83% more!
