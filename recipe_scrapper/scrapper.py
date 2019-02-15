from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def scrap_allrecipes(url):
    """
    Takes a URL for a recipe from All Rrecipes and extracts title, time info, and ingredients
    
    Sample URL: https://www.allrecipes.com/recipe/60598/vegetarian-korma/?internalSource=hub%20recipe&referringContentType=Search
    """
    # Get Recipes html content 
    raw_html = simple_get(url)
    soup = BeautifulSoup(raw_html, 'html.parser')

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

