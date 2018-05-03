from __future__ import division
#import codecademylib
import pandas as pd

#import data from csv
visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

#print to inspect DFs
#print(visits.head())
#print(cart.head())
#print(checkout.head())
#print(purchase.head())

#df.shape[0] is used in favor of len(df) for speed purposes. It doesn't matter
# for this exercise but on a large dataset it would. The zero index is due to the 
# shape being a tuple: (rows, columns).

#Left merge visits and carts. Find number of rows in merged DF
visit_carts = visits.merge(cart, how = 'left')
print('Size of merged visits/carts: {}'.format(visit_carts.shape[0]))

#Find visits with no additions to cart using left merge DF
no_cart_time = visit_carts.cart_time[visit_carts.cart_time.isnull()].shape[0]
print('Visits but no cart: {}'.format(no_cart_time))

#calculate percentage of visitors *not* adding to cart
percent_no_tshirt = no_cart_time * 100 / visit_carts.shape[0]
print('Percent of visitors without adding to cart: {:.2f}%'.format(percent_no_tshirt))

#Left merge cart and checkout DFs. Determine percent of abandoned carts.
cart_checkout = cart.merge(checkout, how = 'left')
no_checkout = cart_checkout.checkout_time[cart_checkout.checkout_time.isnull()].shape[0]\
 * 100 / cart_checkout.shape[0]
print('Percent of carts that do not checkout: {:.2f}%'.format(no_checkout))

#Left merge all data into large DF
all_data = visits.merge(cart, how = 'left')\
.merge(checkout, how = 'left')\
.merge(purchase, how = 'left')
#print(all_data.head())

#Completely ignore all_data and left merge checkout and purchase DFs 
# to find the abandoned checkouts
checkout_purchase = checkout.merge(purchase, how =  'left')
percent_checkout_no_purchase = checkout_purchase[checkout_purchase.purchase_time.isnull()]\
.shape[0] * 100 / checkout_purchase[checkout_purchase.checkout_time.notnull()].shape[0]
print('Percent of users that leave checkout without purchase: {:.2f}%'\
.format(percent_checkout_no_purchase))


#Determine average time to purchase from beginning of visit
all_data['time_to_purchase'] = all_data.purchase_time\
- all_data.visit_time
#print(all_data.time_to_purchase)
print('Average time to purchase: {}'\
      .format(all_data.time_to_purchase.mean()))


