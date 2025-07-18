# Write your solution here

# read the recipe text file
def read_recipe(filename: str):
    recipe_list = []

    with open(filename) as new_file:
        for line in new_file:
            new_line = line.strip()
            recipe_list.append(new_line)
    return recipe_list

# organise the list into a list of lists where the inner list would contain individual recipes
def organize_read_recipe(filename: str):
    unorg_list = read_recipe(filename)
    org_list = []
    individual_recipe = []
    for i in range(len(unorg_list)):
        if unorg_list[i] == "":
            org_list.append(individual_recipe)
            individual_recipe = []
        else:
            individual_recipe.append(unorg_list[i])
            # if the loop reaches the last itme
            if i == len(unorg_list) - 1:
                org_list.append(individual_recipe)
    # turn the numbers from string to integer
    for row in org_list:
        row[1] = int(row[1])
    return org_list

def search_by_name(filename: str, word: str):
    recipe_names_list = []

    recipe_list = organize_read_recipe(filename)

    for row in recipe_list:
        recipe_name = row[0]
        if word.lower() in recipe_name.lower():
            recipe_names_list.append(row[0])

    return recipe_names_list

# search recipe names and print out recipe names that have the word in it
# def search_by_name(filename: str, word: str):
#     recipe_names_list = []

#     recipe_list = read_recipe(filename)

#     for i in range(len(recipe_list)):
#         if word.lower() in recipe_list[i].lower():
#             if i == 0:
#                 recipe_names_list.append(recipe_list[i])
#             elif recipe_list[i - 1] == "":
#                 recipe_names_list.append(recipe_list[i])
#     return recipe_names_list

# search recipes by time and select all recipes under the time designated by user
def search_by_time(filename: str, prep_time: int):
    recipe_list = organize_read_recipe(filename)
    # create a list of strings in the format "[recipe], preparation time [time] min"
    shorter_recipe_list = []
    for row in recipe_list:
        if row[1] <= prep_time:
            recipe_name = row[0]
            time = row[1]
            recipe_and_time = f"{recipe_name}, preparation time {time} min" 
            shorter_recipe_list.append(recipe_and_time)
    return shorter_recipe_list

# search recipes by ingredients, return any recipe that contains said ingredient
def search_by_ingredient(filename: str, ingredient: str):
    recipe_list = organize_read_recipe(filename)
    recipes_with_ingredient = []
    for row in recipe_list:
        for item in row:
            if item == ingredient.lower():
                recipe_name = row[0]
                time = row[1]
                recipe_and_time = f"{recipe_name}, preparation time {time} min"
                recipes_with_ingredient.append(recipe_and_time)
    return recipes_with_ingredient

if __name__ == "__main__":
    # test for part 1
    found_recipes = search_by_name("src/recipes1.txt", "cake")

    for recipe in found_recipes:
        print(recipe)
    
    # test for part 2
    found_recipes_2 = search_by_time("src/recipes1.txt", 20)

    for recipe in found_recipes_2:
        print(recipe)

    # test for part 3
    found_recipes_3 = search_by_ingredient("src/recipes1.txt", "eggs")
    
    for recipe in found_recipes_3:
        print(recipe)

    second test for part 3

    print(organize_read_recipe("src/recipes2.txt"))

    found_recipes_4 = search_by_ingredient("src/recipes2.txt", "fish")

    for recipe in found_recipes_4:
        print(recipe)


 