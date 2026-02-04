import requests

def search_repo(query):
    url = f"https://api.github.com/search/repositories?q={query}"
    r = requests.get(url)
    data = r.json()["items"][:3]

    return [
        {
            "name": repo["name"],
            "stars": repo["stargazers_count"],
            "description": repo["description"]
        }
        for repo in data
    ]
