import requests
import json


#random chuch norris jokes
random_url = "https://api.chucknorris.io/jokes/random"


#list of categories
category_url = "https://api.chucknorris.io/jokes/categories"


#random joke from a specific category
random_category_url = "https://api.chucknorris.io/jokes/random?category={category}"


#text search
search_url = "https://api.chucknorris.io/jokes/search?query={query}"




'''
Part I
The program should welcome the user by displaying a random chuch norris joke
'''
random_url = "https://api.chucknorris.io/jokes/random"
response = requests.get(random_url)
joke = response.json()
joke_text = joke['value']
print("Here is a random Chuck Norris joke for you:")
print(joke_text)
print("\n")


'''
Part II
list the categories to the user and ask to pick a category
'''
response = requests.get("https://api.chucknorris.io/jokes/categories")
categories = response.json()
print("Categories:")
for category in categories:
    print(category)


'''
Part III
Display a joke based on the category picked by the user
'''
selected_category = input("Pick a category: ")
if selected_category in categories:
    response = requests.get(f"https://api.chucknorris.io/jokes/random?category={selected_category}")
    joke = response.json()
    print("Joke:", joke['value'])
else:
    print("Invalid category.")


'''
Part IV
See if you can find a match for the user's favorite chuck norris joke
by asking the user to enter in a few key words of the joke
'''
search_url = "https://api.chucknorris.io/jokes/search?query={query}"
query = input("Enter a few key words of the joke: ")
response = requests.get(search_url.format(query=query))
search_results = response.json()
if search_results['total'] > 0:
    print("Here are some jokes that match your search:")
    for result in search_results['result']:
        print(result['value'])
else:
    print("No jokes found matching your search.")   




