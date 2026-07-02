from assistant.providers.ollama_provider import OllamaProvider

class ChatService:

    def __init__(self, model: str):
        self.provider: OllamaProvider = OllamaProvider(model)

    def ask_streaming(self, prompt: str):
        for streaming_chat in self.provider.chat_stream(prompt):
            yield streaming_chat

    def ask(self, prompt: str):
        response = self.provider.chat(prompt)
        return response
