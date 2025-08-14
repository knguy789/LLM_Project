import requests

BACKEND_URL = "http://localhost:8000/chat"

print("Research Agent - Local LLaMA3 Chat")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["quit", "exit", "stop", "terminate"]:
        break

    try:
        # send prompt in expected shape
        res = requests.post(BACKEND_URL, json={"prompt": user_input})
        res.raise_for_status()
        data = res.json()
        print("AI:", res.json().get("response", ""))
    except Exception as e:
        print(f"Error talking to backend: {e}")