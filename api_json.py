
import requests
import json

def get_allrepos():
    all_repos = requests.get('https://api.github.com/orgs/lodash/repos').text.encode()
    repos_data = json.loads(all_repos) # Converts String into a Python List and saves it in a new variable.
    return repos_data  # This function returns data output to pass to the other function below


# For Loop through the data from the get_allrepos() and grab all pull requests
def get_pulls():
    data = get_allrepos()  

    for pulls in data:
        all_pulls = (pulls['pulls_url'])
        #print(all_pulls)  

get_pulls()
