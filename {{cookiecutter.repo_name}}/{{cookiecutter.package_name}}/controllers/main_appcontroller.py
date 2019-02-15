from ..ui.mainwindow import {{ cookiecutter.mainwindow_name }}
import logging


class MainAppController:

    def __init__(self):
        self.mainwindow = {{cookiecutter.mainwindow_name}}(parent=self)

    def run(self):
        logging.debug("Show UI Application")
        self.mainwindow.show()
