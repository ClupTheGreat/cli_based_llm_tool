from assistant.providers.ollama_provider import OllamaProvider
import logging

# Creating log object
logger = logging.getLogger(__name__)

class ChatService:

    def __init__(self, model: str):
        logger.info("Initializing ChatService")
        self.provider: OllamaProvider = OllamaProvider(model)

    def ask_streaming(self, prompt: str):
        try:
            for streaming_chat in self.provider.chat_stream(prompt):
                yield streaming_chat
            logger.info("Streaming response recieved from Ollama")
        except Exception:
            logger.error("Error while streaming output from OllamaProvider")
            raise

    # Probably wont be using
    def ask(self, prompt: str):
        response = self.provider.chat(prompt)
        return response
