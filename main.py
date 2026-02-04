from agents.planner import planner_agent
from agents.executor import executor_agent
from agents.verifier import verifier_agent

if __name__ == "__main__":
    task = input("Enter your task: ")

    plan = planner_agent(task)
    execution = executor_agent(plan)
    final_output = verifier_agent(execution)

    print("\nFINAL OUTPUT:\n", final_output)
