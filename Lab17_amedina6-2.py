"""
Program: Most-starred JavaScript Repositories.
Author: Alberto Medina
Purpose: Retrieve live Github API data and create an interactive Plotly visualization
    of popular JavaScript repositories.
Date: Auguts 13,2026"""




import requests
import plotly.express as ex


url = "https://api.github.com/search/repositories"
url += "?q=language:javascript+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
response = requests.get(url, headers=headers)
print(f"Status Code: {response.status_code}")

response_dict = response.json()

print(f"Total Repo: {response_dict['total_count']}")
print(f"Complete results: {not response_dict['incomplete_results']}")

repo_dicts = response_dict["items"]
print(f"Repositories returned: {len(repo_dicts)}")


repo_links, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    repo_name = repo_dict["name"]
    repo_url = repo_dict["html_url"]
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict["stargazers_count"])

    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    hover_text = f"{owner}<br>{description}"
    hover_texts.append(hover_text)


title = "Most-Starred JavaScript Projects on Github"
labels = {"x": "Repository", "y": "Stars"}

fig = ex.bar(
    x=repo_links,
    y=stars,
    hover_name=hover_texts,
    title=title,
    labels=labels,
)

fig.write_html("javascripts_repos.html")

fig.write_html("javascripts_repos.html")
fig.write_image(
    "javascripts_repos.png",
    width=1600,
    height=900,
    scale=2
)

fig.show()