import requests

def chatbot_response(user_input):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": f"You are a supportive mental health chatbot. Reply in the same language as user. User: {user_input}",
                "stream": False
            }
        )

        return response.json()["response"]

    except Exception as e:
        print("Error:", e)
        return "I'm here for you."