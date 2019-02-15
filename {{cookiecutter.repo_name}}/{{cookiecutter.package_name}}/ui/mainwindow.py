from PyQt5.QtWidgets import (QAction, QApplication, QFileDialog, QToolBar, QMainWindow)

from {{cookiecutter.package_name}}.ui_designer.ui_mainwindow import Ui_MainWindow

class {{ cookiecutter.mainwindow_name }}(QMainWindow):
    """Create the main window that stores all of the widgets necessary for the application."""

    def __init__(self, parent=None):
        """Initialize the components of the main window."""
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.resize(1024, 768)
        self.setWindowTitle('{{ cookiecutter.application_title }}')
        # window_icon = pkg_resources.resource_filename('{{ cookiecutter.package_name }}.images',
        #                                               'ic_insert_drive_file_black_48dp_1x.png')
        # self.ui.setWindowIcon(QIcon(window_icon))

        # self.widget = QWidget()
        # self.layout = QHBoxLayout(self.widget)
        #
        # self.menu_bar = self.menuBar()
        # self.about_dialog = AboutDialog()
        #
        # {% if cookiecutter.insert_statusbar == 'yes' -%}
        # self.status_bar = self.statusBar()
        # self.status_bar.showMessage('Ready', 5000)
        # {%- endif %}
        #
        # self.file_menu()
        # self.help_menu()
        #
        # {% if cookiecutter.insert_toolbar == 'yes' -%}
        # self.tool_bar_items()
        # {%- endif %}

    def file_menu(self):
        """Create a file submenu with an Open File item that opens a file dialog."""
        self.file_sub_menu = self.menu_bar.addMenu('File')

        self.open_action = QAction('Open File', self)
        self.open_action.setStatusTip('Open a file into {{ cookiecutter.application_title }}.')
        self.open_action.setShortcut('CTRL+O')
        self.open_action.triggered.connect(self.open_file)

        self.exit_action = QAction('Exit Application', self)
        self.exit_action.setStatusTip('Exit the application.')
        self.exit_action.setShortcut('CTRL+Q')
        self.exit_action.triggered.connect(lambda: QApplication.quit())

        self.file_sub_menu.addAction(self.open_action)
        self.file_sub_menu.addAction(self.exit_action)

    def help_menu(self):
        """Create a help submenu with an About item tha opens an about dialog."""
        self.help_sub_menu = self.menu_bar.addMenu('Help')

        self.about_action = QAction('About', self)
        self.about_action.setStatusTip('About the application.')
        self.about_action.setShortcut('CTRL+H')
        self.about_action.triggered.connect(lambda: self.about_dialog.exec_())

        self.help_sub_menu.addAction(self.about_action)

    {% if cookiecutter.insert_toolbar == 'yes' -%}
    def tool_bar_items(self):
        """Create a tool bar for the main window."""
        self.tool_bar = QToolBar()
        self.addToolBar(Qt.TopToolBarArea, self.tool_bar)
        self.tool_bar.setMovable(False)

        open_icon = pkg_resources.resource_filename('{{ cookiecutter.package_name }}.images',
                                                    'ic_open_in_new_black_48dp_1x.png')
        tool_bar_open_action = QAction(QIcon(open_icon), 'Open File', self)
        tool_bar_open_action.triggered.connect(self.open_file)

        self.tool_bar.addAction(tool_bar_open_action)
    {%- endif %}

    def open_file(self):
        """Open a QFileDialog to allow the user to open a file into the application."""
        filename, accepted = QFileDialog.getOpenFileName(self, 'Open File')

        if accepted:
            with open(filename) as file:
                file.read()
