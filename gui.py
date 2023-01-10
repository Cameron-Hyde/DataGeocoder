import sys
from PyQt6.QtWidgets import (
    QFileDialog,
    QInputDialog,
    QMainWindow,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

    def get_file_path(self):
        #Open file dialog and return selected file path
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Excel/CSV file", "", "")
        return file_name

    def get_input_data(self):
        #Open multiple input dialogs and return user inputs for file name
        #owner column, address column, sqft column
        file_name = self.get_file_path()
        owner_col, ok = QInputDialog.getText(
            self,
            "InPuT",
            "Enter the name of the column in the file that contains the owners' names:",
        )
        if not ok:
            sys.exit()
        address_col, ok = QInputDialog.getText(
            self,
            "InPuT",
            "Enter the name of the column in the file that contains the addresses:",
        )
        if not ok:
            sys.exit()
        sqft_col, ok = QInputDialog.getText(
            self,
            "InPuT",
            "Enter the name of the column in the file that contains the sqft data (leave blank if not applicable):",
        )
        if not ok:
            sys.exit()
        return file_name, owner_col, address_col, sqft_col
