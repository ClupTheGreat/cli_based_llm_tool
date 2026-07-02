from assistant.cli.parser import cli_parser
from assistant.services.chat import ChatService

def run():
    # We will eventually accept a model from the user if provided, but we will use a placeholder model
    # for now.
    
    # Initialize chat model
    placeholder_model = "qwen3.5:9b"
    chat_service = ChatService(model=placeholder_model)
    
    # Accept arguments from the user
    args = cli_parser()
    if args is None:
        print("Please enter an argument")
    else:
        for piece in chat_service.ask_streaming(args):
            print(piece, end='', flush=True)
        print("\n")
