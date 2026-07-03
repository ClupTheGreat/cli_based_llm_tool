from assistant.cli.commands import run
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s %(name)s: %(message)s]',
    handlers=[
        logging.FileHandler('logs/application.log')
    ]
)

def main():
    run()


if __name__ == "__main__":
    main()
