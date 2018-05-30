import numpy as np
import fetchmaker
from scipy.stats import binom_test, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# Testing out the functions
# get_tail_length, get_color, get_age,  get_is_rescue
# all take a breed as an input
rottweiler_tl = fetchmaker.get_tail_length('rottweiler')
print('Avg Rottweiler weight: {:.2f}'.format(np.mean(rottweiler_tl)))
print('Std Dev: {:.2f}\n'.format(np.std(rottweiler_tl)))

# 8% of dogs are historically rescues
# Do Whippets deviate significantly from that?
whippet_rescue = fetchmaker.get_is_rescue('whippet')

# Get number of whippet rescues and total whippets
num_whippet_rescues = np.count_nonzero(whippet_rescue)
assert np.sum(whippet_rescue) == num_whippet_rescues
num_whippets = whippet_rescue.size

print(binom_test(num_whippet_rescues, n = num_whippets, p=0.08))
print('Unable to reject hypothesis that whippets have avg likelihood of being a rescue.\n')

# Determine if there is a sig. diff. between
# the weights of whippets, terriers and pitbulls
weights = []
for breed in ['whippet', 'terrier','pitbull']:
    weights.append(fetchmaker.get_weight(breed))
print(f_oneway(*weights).pvalue)
print('Reject the null hypothesis that whippets, terriers and pitbulls have the same average weight.')

# Determine which breed is different
labels =  ['whippet']*len(weights[0]) + \
            ['terrier']*len(weights[1]) + \
            ['pitbull']*len(weights[2])

tukey_range = pairwise_tukeyhsd(np.concatenate(weights),
                       labels,
                         0.05)
count = 0
for i in range(len(tukey_range.groupsunique)-1):
    for j in range(i+1, len(tukey_range.groupsunique)):
      print('Reject {}-{}? {}'.format(
      tukey_range.groupsunique[i],
      tukey_range.groupsunique[j],
      tukey_range.reject[count]
    	))
      count += 1
print('\n')
# Terrier is significantly different
for key, breed in enumerate(['whippet', 'terrier','pitbull']):
    print('{}: {} +/- {:.2f}'.format(
      breed,
      np.mean(weights[key]),
      np.std(weights[key])
    ))

poodle_colors = fetchmaker.get_color('poodle')
shihtzu_colors = fetchmaker.get_color('shihtzu')

colors = ['black', 'brown', 'gold', 'grey', 'white']
color_table = np.array(
    [[np.count_nonzero(poodle_colors == color) for color in colors],
    [np.count_nonzero(shihtzu_colors == color) for color in colors]]).transpose()

print('\n The p value for the hypothesis that poodles and shihtzus have' +
        ' significantly different color breakdowns is {:.4f} '.format(
        chi2_contingency(color_table)[1]
        ))
