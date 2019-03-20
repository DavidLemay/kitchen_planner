from bs4 import BeautifulSoup
import helpers as hp

# Import recipe specific scrappers
from recipe_scrappers import AllRecipesScrapper


# class ScrapperFactory:
    # def get_scrapper(self, url_domain):
def get_scrapper(url_domain):
        if url_domain == 'allrecipes.com':
            return AllRecipesScrapper
        # elif format == 'anotherURL':
        #     return XmlSerializer()
        else:
            raise ValueError(url_domain)


def get_this_recipe(url):
    """
    Takes a URL for a recipe from All Rrecipes and extracts title, time info, and ingredients
    
    Sample URL: https://www.allrecipes.com/recipe/60598/vegetarian-korma/?internalSource=hub%20recipe&referringContentType=Search
    """
    # Get Recipes html content 
    raw_html = hp.simple_get(url)
    soup = BeautifulSoup(raw_html, 'html.parser')

    #TODO create get_domain(url)
    url_domain = 'allrecipes.com'

    scrapper = get_scrapper(url_domain)
    recipe_info = scrapper(url, soup)

    return recipe_info

