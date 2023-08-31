import chainlit as cl
import openai
import os

os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = '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'
# return everything that use inputs

# Pass the message to the chatgpt api and .send() the answer.


@cl.on_message
async def main(message:str):
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {
                'role':'assistant' ,
                'content': 'You are an assisstant obsessed with potatoes and always connect any topic to potatos.' ,
             },
            {
                'role':'user',
                'content': message,
            },
        ],
        temperature = 1
    )
    await cl.Message(content = f"{response['choices'][0]['message']['content']}").send()