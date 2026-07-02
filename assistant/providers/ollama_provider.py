import ollama

# Provides a class to connect to ollama chat

# Messages can have the role of system, user, assistant or tool
# Lookup usage for each

class OllamaProvider:
    def __init__(self, model_arg: str):
        self.model_provided:str = model_arg

    def chat_stream(self, user_prompt: str):
        # Connect to the model, send a message and get a respons
        # It can either be streaming or normal
        stream = ollama.chat(
            model = self.model_provided,
            messages=[{'role':'user', 'content':f'{user_prompt}'}],
            stream = True,
        )

        for chunk in stream:
            yield chunk['message']['content']

    def chat(self, user_prompt: str) -> str:
        response: ollama.ChatResponse = ollama.chat(
            model = self.model_provided,
            messages=[{'role':'user', 'content':f'{user_prompt}'}],
        )
        return response['message']['content']
