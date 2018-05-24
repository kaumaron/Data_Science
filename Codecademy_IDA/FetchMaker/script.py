import numpy as np
import fetchmaker
from scipy.stats import binom_test, f_oneway
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
print(pairwise_tukeyhsd(np.concatenate(weights),
                       labels,
                         0.05))


# Terrier is significantly different
for key, breed in enumerate(['whippet', 'terrier','pitbull']):
    print('{}: {}'.format(breed, np.mean(weights[key])))
