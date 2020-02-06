#!/usr/bin/python
import math

def recipe_batches(recipe, ingredients):

    # Convert dictionary values to lists
    _recipe = list(recipe.values())
    _ingredients = list(ingredients.values())

    # If not all ingredients are present, return 0
    if(len(_ingredients) < len(_recipe)):
        return 0

    # Create an array to recipe[i] // ingredients[i]  
    batch_counts = [0] * len(_recipe)

    # Fill the array with those quotients
    for i in range(len(_recipe)):
        batch_counts[i] = _ingredients[i] // _recipe[i]

    # Assign the first element as the smallest value
    min_batch_count = batch_counts[0]

    # Compare each value to the smallest value and 
    # replace the smallest value if the compaired value is smaller
    for i in range(1, len(_recipe)):
        if batch_counts[i] < min_batch_count:
            min_batch_count = batch_counts[i]

    # The smallest value in that list is our answer
    return min_batch_count

if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    _recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    _ingredients = {'milk': 132, 'butter': 480, 'flour': 15}
    print("{batches} batches can be made from the available _ingredients: {_ingredients}.".format(
        batches=recipe_batches(_recipe, _ingredients), _ingredients=_ingredients))
