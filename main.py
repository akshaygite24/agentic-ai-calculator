from agent import create_agent_instance

agent = create_agent_instance()

while True:
    query = input("Ask: ")

    if query.lower() == "exit":
        break

    if not query.strip():
        print("please enter a valid query.")
        continue

    response = agent.invoke({
        "messages": [
            {"role": "user", "content": query}
        ]
    })
    print(f"Logs : {response}/n/n")
    print(response["messages"][-1].content)