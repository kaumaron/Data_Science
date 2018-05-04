import numpy as np

#for recipes.csv
recipe_columns = ['flour', 
                  'sugar', 
                  'eggs', 
                  'milk', 
                  'butter']
recipe_rows = ['cupcakes', 
               'pancakes', 
               'cookie', 
               'bread']

# add in cupcake recipe
cupcakes = np.array([2, 0.75, 2, 1, 0.5])

#import all recipes from csv
recipes = np.genfromtxt('recipes.csv', delimiter = ',')
print(recipes)

#find the eggs in the recipes and determine 
#which recipes require exactly one egg
eggs = recipes[:,2]
print('\nThese recipes require exactly one egg:')
for k,v in enumerate(eggs == 1):
    if v == True:
    	print(recipe_rows[k])
      
#find recipe for cookies
cookies = recipes[2,:]

#amount of ingredients for double batch of cupcakes
double_batch = cupcakes * 2

#add items for cookies and cupcakes to grocery list
grocery_list = cookies + double_batch
print('\nGrocery List:\n' + '\n'.join(
  [x+': ' + str(y) for x,y in
   zip(recipe_columns,grocery_list)]))
