def call_llm(prompt):
    # Mocked planner response (LLM simulated)
    return """
    {
      "steps": [
        {
          "tool": "github",
          "action": "search_repo",
          "input": "AI"
        },
        {
          "tool": "weather",
          "action": "get_weather",
          "input": "Delhi"
        }
      ]
    }
    """



