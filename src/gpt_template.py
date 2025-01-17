import openai
from openai import OpenAI
import os


def chat(user_input, content):
    system_prompt = "You are a ..."
    user_prompt = f"""
    Question: <{user_input}>
    
    Content: <{content}>

    Answer:
    """
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = OpenAI().chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                'role': 'system',
                'content': system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1
    )

    return response.choices[0].message['content']
