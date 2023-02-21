import requests
from bs4 import BeautifulSoup
import csv

# Make the request
url = 'https://github.com/trending'
def request_github_trending(url):
    result = requests.get(url)
    return result


# Extract the data
from bs4 import BeautifulSoup

def extract(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    repos_html = soup.find_all('h1', class_="h3 lh-condensed")
    return repos_html


# Transform the data into a list of dictionaries
def transform(html_repos):
    repos_data = []
    for repos in html_repos:
        repo_name = repos.find('a')
        developer = repos.find('span', class_='text-normal')
        nbr_stars = repos.find('a', class_='muted-link mr-3')
        repos_data.append({'developer': developer, 'repository_name': repo_name, 'nbr_stars': nbr_stars})
    return repos_data

# Format the data into a CSV file
def format(repositories_data):
    csv_string = 'Developer,Repository Name,Number of Stars\n'
    for repo in repositories_data:
        csv_string += f"{repo['developer']}, repo{['repository_name']}, repo{['nbr_stars']}\n"
    return csv_string

# print result
if __name__ == '__main__':
    page = request_github_trending(url)
    html_repos =extract(page)
    repositories_data = transform(html_repos)
    my_result = format(repositories_data)
    print(my_result)