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
# for this exercise but on a large dataset it would. The zero index is due to
# shape being a tuple: (rows, columns).

#Left merge visits and carts. Find number of rows in merged DF
visit_carts = visits.merge(cart, how = 'left')
print('Size of merged visits/carts: {}'.format(visit_carts.shape[0]))

#Find visits with no additions to cart using left merge DF
no_cart_time = visit_carts.cart_time[visit_carts.cart_time.isnull()].shape[0]
print('Visits but no cart: {}'.format(no_cart_time))

#calculate percentage of visitors *not* adding to cart
percent_no_tshirt = no_cart_time * 100 / visit_carts.shape[0]
print('Percent of visitors without adding to cart: {:.2f}%'\
    .format(percent_no_tshirt))

#Left merge cart and checkout DFs. Determine percent of abandoned carts.
cart_checkout = cart.merge(checkout, how = 'left')
no_checkout = cart_checkout.checkout_time[cart_checkout.checkout_time\
    .isnull()].shape[0] * 100 / cart_checkout.shape[0]
print('Percent of carts that do not checkout: {:.2f}%'.format(no_checkout))

#Left merge all data into large DF
all_data = visits.merge(cart, how = 'left')\
.merge(checkout, how = 'left')\
.merge(purchase, how = 'left')
#print(all_data.head())

#Completely ignore all_data and left merge checkout and purchase DFs 
# to find the abandoned checkouts
checkout_purchase = checkout.merge(purchase, how =  'left')
percent_checkout_no_purchase = checkout_purchase[checkout_purchase\
    .purchase_time.isnull()].shape[0] * 100 / \
    checkout_purchase[checkout_purchase.checkout_time.notnull()].shape[0]
print('Percent of users that leave checkout without purchase: {:.2f}%'\
.format(percent_checkout_no_purchase))


#Determine average time to purchase from beginning of visit
all_data['time_to_purchase'] = all_data.purchase_time\
- all_data.visit_time
#print(all_data.time_to_purchase)
print('Average time to purchase: {}'\
      .format(all_data.time_to_purchase.mean()))

#
#Recalculate using only all_data and unique visitors
#
print('\nThe all_data DF has {} entries.'.format(
                                all_data.user_id.unique().shape[0])
                                )

no_cart_time_2 = all_data[all_data.cart_time.isnull()].user_id.unique()\
            .shape[0]
percent_no_tshirt_2 = no_cart_time * 100 / all_data[all_data\
    .visit_time.notnull()].user_id.unique().shape[0]
print('*Percent of visitors without adding to cart: {:.2f}%'\
    .format(percent_no_tshirt_2))

no_checkout_2 = all_data[all_data.checkout_time.isnull() & all_data.cart_time\
    .notnull()].user_id.unique().shape[0] * 100 /\
    all_data[all_data.cart_time.notnull()].user_id.unique().shape[0]
print('*Percent of carts that do not checkout: {:.2f}%'.format(no_checkout_2))

percent_checkout_np_2 = all_data[all_data.purchase_time.isnull() & all_data\
    .checkout_time.notnull()].user_id.unique().shape[0] /\
        all_data[all_data.checkout_time.notnull()].user_id.unique().shape[0] \
        * 100
print('*Percent of users that leave checkout without purchase: {:.2f}%'\
    .format(percent_checkout_np_2))
