import re
import json
from llm.llm_client import call_llm

def planner_agent(user_task):
    prompt = f"""
Convert the task into a JSON plan.

Task: {user_task}

Return ONLY JSON:
{{
  "steps": [
    {{
      "tool": "github",
      "action": "search_repo",
      "input": "AI"
    }},
    {{
      "tool": "weather",
      "action": "get_weather",
      "input": "Delhi"
    }}
  ]
}}
"""
    text = call_llm(prompt)
    json_text = re.search(r"\{[\s\S]*\}", text).group()
    return json.loads(json_text)

