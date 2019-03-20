from bs4 import BeautifulSoup
import helpers as hp

# Import recipe specific scrappers
from recipe_scrappers import factory

def get_this_recipe(url):
    """
    Takes a recipe URL and returns key info (ingredients, time info, etc.)
    """
    print("# Starting scrapper...")
    print(f"# getting ingredients for '{url}'")

    # Get html content and prepare it for scrapping 
    raw_html = hp.simple_get(url)
    soup = BeautifulSoup(raw_html, 'html.parser')

    # Get hostname (i.e. 'www.allrecipes.com')
    hostname = hp.get_hostname(url)

    # Get a scrapper that matches hostname and pass url+soup for scrapping
    scrapper = factory.get_scrapper(hostname)
    recipe_info = scrapper(url, soup)

    if recipe_info:
        print("# Sucess!")
        print(recipe_info)
        return recipe_info
    else:
        print("Error!")


"""
    Run Script
"""
# Recipe url (Feel free to change the test URL)
TEST_URL = 'https://www.allrecipes.com/recipe/60598/vegetarian-korma/?internalSource=hub%20recipe&referringContentType=Search'

# Request recipe! 
get_this_recipe(TEST_URL)