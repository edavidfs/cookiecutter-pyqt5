import sys

import pkg_resources
import logging

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (QApplication, QDialog,
                             QLabel, QVBoxLayout)
from {{ cookiecutter.package_name }}.controllers.main_appcontroller import MainAppController


class AboutDialog(QDialog):
    """Create the necessary elements to show helpful text in a dialog."""

    def __init__(self, parent=None):
        """Display a dialog that shows application information."""
        super(AboutDialog, self).__init__(parent)

        self.setWindowTitle('About')
        help_icon = pkg_resources.resource_filename('{{ cookiecutter.package_name }}.images',
                                                    'ic_help_black_48dp_1x.png')
        self.setWindowIcon(QIcon(help_icon))
        self.resize(300, 200)

        author = QLabel('{{ cookiecutter.full_name }}')
        author.setAlignment(Qt.AlignCenter)

        icons = QLabel('Material design icons created by Google')
        icons.setAlignment(Qt.AlignCenter)

        github = QLabel('GitHub: {{ cookiecutter.github_username }}')
        github.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignVCenter)

        self.layout.addWidget(author)
        self.layout.addWidget(icons)
        self.layout.addWidget(github)

        self.setLayout(self.layout)


if __name__ == '__main__':

    logging.basicConfig(level=logging.DEBUG,
                        format='%(threadName)-10s - %(asctime)s - %(message)s')


    application = QApplication(sys.argv)
    controller = MainAppController()
    controller.run()
    sys.exit(application.exec_())
