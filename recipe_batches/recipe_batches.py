#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    _recipe = list(recipe.values())
    _ingredients = list(ingredients.values())
    print(f"_recipe: {_recipe}")
    print(f"_ingredients: {_ingredients}")
    if(len(_ingredients) < len(_recipe)):
        return 0

    batch_counts = [0] * len(_recipe)

    for i in range(len(_recipe)):
        batch_counts[i] = _ingredients[i] // _recipe[i]

    print(f"batch_counts: {batch_counts}")
    min_batch_count = batch_counts[0]

    for i in range(1, len(_recipe)):
        if batch_counts[i] < min_batch_count:
            min_batch_count = batch_counts[i]
    return min_batch_count


if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    _recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    _ingredients = {'milk': 132, 'butter': 480, 'flour': 15}
    print("{batches} batches can be made from the available _ingredients: {_ingredients}.".format(
        batches=recipe_batches(_recipe, _ingredients), _ingredients=_ingredients))
