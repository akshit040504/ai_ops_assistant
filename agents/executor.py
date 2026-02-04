from tools.github_tool import search_repo
from tools.weather_tool import get_weather

def executor_agent(plan):
    results = []

    for step in plan["steps"]:
        if step["tool"] == "github":
            results.append(search_repo(step["input"]))
        elif step["tool"] == "weather":
            results.append(get_weather(step["input"]))

    return results
