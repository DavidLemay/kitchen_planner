# kitchen_planner
A meal/groceries-shopping planifier. Currently just a scrapper to get ingredients from popular food sites, merges ingredients from different recipes, and returns a shopping list. 


## Set up virtual environment (Linux)
1. Make sure you have python3, if not download/install it with [pyenv](https://github.com/pyenv/pyenv-installer) 
2. Create a virtual environment
    ```bash
    # From the root directory
    $ python3 -m venv .

    # Activate venv
    $ source venv/bin/activate

    # Check your python and pip version (python should be 3.X, and your pip should match that python version)
    (venv)$ python -V
    (venv)$ pip -V
    
    # Install requirements
    (venv)$ pip install requirements.txt

    ```
3. Quick test.
    ```bash
    # Run script 
    (venv) $ python main.py
    ```
    *It uses a default url (TEST_URL) of a recipe, located at the end of main.py. It can be modified for testing.

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