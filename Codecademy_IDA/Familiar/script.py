import familiar
import numpy as np
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency

avg_life_exp = 71
#Load data and test for significance compared to 71 yrs
vein_pack_lifespans = familiar.lifespans(package = 'vein')
vein_pack_test = ttest_1samp(vein_pack_lifespans, avg_life_exp)

#Report if lifespan is significantly greater than 71 yrs
if vein_pack_test.pvalue < 0.05 and\
    np.mean(vein_pack_lifespans) > avg_life_exp:
    print('The Vein Pack is Proven To Make You Live Longer!')
else:
    print('The Vein Pack Is Probably Good For You Somehow!')


# Load artery data
artery_pack_lifespans = familiar.lifespans(package = 'artery')
artery_pack_test = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
package_comparison_results = artery_pack_test.pvalue

# Report results
if artery_pack_test.pvalue < 0.05 and\
    np.mean(artery_pack_lifespans) > avg_life_exp:
    print('the Artery Package guarantees even stronger results!')
else:
    print('the Artery Package is also a great product!'.title())
  
iron_contingency_table = familiar.iron_counts_for_package()
iron_pvalue = chi2_contingency(iron_contingency_table)[1]

# Report results
if iron_pvalue < 0.05:
  print('The Artery Package Is Proven To Make You Healthier!')
else:
  print('While We Can\'t Say The Artery Package Will Help You,' +\
        ' I Bet It\'s Nice!')
