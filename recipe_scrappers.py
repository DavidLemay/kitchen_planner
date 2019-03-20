class ScrapperFactory:
    """ 
    An object factory that decides which scrapper to use for a given recipe link provided by the user
    
    It is in charge of:
    - Provides a method to register scrappers by providing a scrapper class and a hostname
    - Keep track of all recipe sites supported and the respective scrapper registered with that site
    - Determines which scrapper to use based on a given url 
    - #TODO add extract_hostname(url) method
    
    param
    :_scrappers = a dictionary of scrappers {hostname:scrapper}
    :hostname = the domain of a specific recipe site (i.e. 'allrecipes.com') 
    :scrapper   = a recipe specific scrapper Class
    """
    def __init__(self):
        self._scrappers = {}

    def register_scrapper(self, hostname, scrapper):
        self._scrappers[hostname] = scrapper

    def get_scrapper(self, hostname):
        """ Takes a recipe hostname and returns a registered scrapper that supports, or fails """ 
        scrapper = self._scrappers.get(hostname)
        if not scrapper:
            raise ValueError(hostname)
        return scrapper


"""
    Recipe specific Scrappers go bellow
"""

def AllRecipesScrapper(url, soup):
    """ Scrapper for allrecipes.com """
    # get title
    title = soup.title.text[:-17] # -17 to remove site's name

    # get ingredients
    li_checklist = soup.find_all('li', attrs={"class": "checkList__line"})
    ingredients = [li.span.text for li in li_checklist]

    # get time info
    t_prep = soup.find('time', attrs={"itemprop": "prepTime"})
    t_cook = soup.find('time', attrs={"itemprop": "prepTime"})
    t_total = soup.find('time', attrs={"itemprop": "prepTime"})

    time_info = {
        # Transform to int and remove ' m' at the end (with -2)
        "prep_time": int(t_prep.text[:-2]),
        "cook_time": int(t_cook.text[:-2]),
        "total_time": int(t_total.text[:-2]),
    }

    # Output
    recipe_info = {
        'title': title,
        'ingredients': ingredients,
        'time_info': time_info,
        'url': url
    }
    return recipe_info


## ADD more recipe specific scrappers here  


"""
    Register the scrapper with ScrapperFactory
"""
factory = ScrapperFactory()
factory.register_scrapper('www.allrecipes.com', AllRecipesScrapper)