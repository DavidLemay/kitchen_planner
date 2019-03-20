# kitchen_planner

## Set up virtual environment
... coming Soon

## Run scripts in terminal
```bash
# Activate venv
$ source venv/bin/activate

# Start python in terminal
(venv) $ python
```
```python
# Import application main.py
import main

# pass valid url
url = 'https://www.allrecipes.com/recipe/60598/vegetarian-korma/?internalSource=hub%20recipe&referringContentType=Search'

# Request recipe! 
main.get_this_recipe(url)
```