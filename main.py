from app import App
from utils.hooks import *


def main():
    app = App()
    help_setup()
    app.input_loop()
    while not app.exit:
        app.main_loop()


if __name__ == "__main__":
    main()

