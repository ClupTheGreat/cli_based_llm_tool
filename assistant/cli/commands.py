# imports for application
from assistant.cli.parser import cli_parser
from assistant.services.chat import ChatService

# general imports
import itertools
import threading
import sys
import time

def animate(loading: threading.Event):
    # Simple CLI animation, loading spinner
    for c in itertools.cycle(['|','/','-','\\']):
        if loading.is_set():
            break
        sys.stdout.write('\rthinking ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\n')

def run():
    # We will eventually accept a model from the user if provided, but we will use a placeholder model
    # for now.
    
    # Initialize chat model
    placeholder_model = "qwen3.5:9b"
    chat_service = ChatService(model=placeholder_model)
    
    # Accept arguments from the user
    args = cli_parser()

    # Flag for thinking animation thread
    loading = threading.Event() 

    if args is None:
        print("Please enter an argument")
    else:
        # Starting another thread for thinking animation to not block the
        # main thread.
        thinking_thread = threading.Thread(target=animate, args=(loading,))
        thinking_thread.start()

        for piece in chat_service.ask_streaming(args):

            # Handles the empty spaces in the cli with thinking animation
            if piece != '':
                loading.set() 
                thinking_thread.join()

            # Printing as a stream from LLM
            print(piece, end='', flush=True)
        print("\n")
