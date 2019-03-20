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