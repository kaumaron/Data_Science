import noshmishmosh
import numpy as np
import scipy

# Determine baseline, minimum_detectible_effect and stat_sig
all_visitors = noshmishmosh.customer_visits
paying_visitors = noshmishmosh.purchasing_customers
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)
baseline_percent = paying_visitor_count / total_visitor_count
print('Baseline Percent: {}%'.format(baseline_percent * 100))

payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)
new_customers_needed = np.ceil(1240 / average_payment)
percentage_point_increase = new_customers_needed / total_visitor_count
print('Percentage Point Increase: {}'.format(percentage_point_increase * 100))

minimum_detectable_effect = percentage_point_increase / baseline_percent
print('Minimum Detectable Effect: {:.2f}%'.format(
        minimum_detectable_effect * 100))

stat_sig = 0.90
ab_sample_size = 290

def sample_size(pop = 100000, error = 0.03, base = 0.2, stat_sig = 0.85):
    z_scores = {0.80: 1.28, 0.85: 1.44, 0.90: 1.65, 0.95: 1.96, 0.99: 2.58}
    z = z_scores[stat_sig]
    factor = 2 * (z + 1.28) ** 2
    n_0 = np.sqrt(base * (1 - base)) / (error * base)
    return np.ceil(factor * n_0 ** 2)

print('Sample Size: {}'.format(
        sample_size(error = minimum_detectable_effect,
            base = baseline_percent,
            stat_sig = 0.90))
            )
