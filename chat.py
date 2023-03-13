# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.api_key = "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"

def prompt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens = 60,
        messages=[
                {"role": "system", "content": "You are a Dall-E prompt generator. You will be given music genres and you would create a Dall-E prompt. You would return the Dall-E prompt only"},
                {"role": "user", "content": "Generate me a Dall-E prompt for jazz music"},
                {"role": "assistant", "content": "Dall-E image: An image of a dimly lit jazz club, with a pianist in the foreground playing a baby grand piano, while a hazy crowd watches on in the background."},
                {"role": "user", "content": f"Generate me a Dall-E prompt for {prompt} music"}
            ]
        )

    message = response['choices'][0]['message']['content']
    print(message)
    return message
