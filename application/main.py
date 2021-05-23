from application.UI import MainWindow
import os
from application.util.config import Config



if __name__ == "__main__":
    config = Config(os.path.join(os.path.dirname(__file__), "..","output"))
    MainWindow.main(config)