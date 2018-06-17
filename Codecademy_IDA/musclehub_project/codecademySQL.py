import os
import sqlite3
import pandas as pd

# Clear example.db if it exists
if os.path.exists('example.db'):
    os.remove('example.db')
    
# Create a database
conn = sqlite3.connect('example.db')

# Load some csv data
visits = pd.read_csv('visits.csv')
fitness_tests = pd.read_csv('fitness_tests.csv')
applications = pd.read_csv('applications.csv')
purchases = pd.read_csv('purchases.csv')

# Add the data to our database
visits.to_sql('visits', conn, dtype={
    'first_name':'VARCHAR(256)',
    'last_name':'VARCHAR(256)',
    'email':'VARCHAR(256)',
    'gender':'VARCHAR(256)',
	'visit_date': 'DATE'
})
fitness_tests.to_sql('fitness_tests', conn, dtype={
    'first_name':'VARCHAR(256)',
    'last_name':'VARCHAR(256)',
    'email':'VARCHAR(256)',
    'gender':'VARCHAR(256)',
	'fitness_test_date': 'DATE'
})
applications.to_sql('applications', conn, dtype={
    'first_name':'VARCHAR(256)',
    'last_name':'VARCHAR(256)',
    'email':'VARCHAR(256)',
    'gender':'VARCHAR(256)',
	'application_date': 'DATE'
})
purchases.to_sql('purchases', conn, dtype={
    'first_name':'VARCHAR(256)',
    'last_name':'VARCHAR(256)',
    'email':'VARCHAR(256)',
    'gender':'VARCHAR(256)',
	'purchases_date': 'DATE'
})

# Make a convenience function for running SQL queries
def sql_query(query):
    try:
        df = pd.read_sql(query, conn)
    except Exception, e:
        print e.message
    return df
