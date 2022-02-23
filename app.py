import os
import sys
import logging
import multiprocessing

from PySide6.QtGui import QIntValidator
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog

from services import FTPManager
from design.ui_mainwindow import Ui_MainWindow

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
os.environ['JOBLIB_MULTIPROCESSING'] = '0'


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('SimpleFTPServer')
        self.onlyInt = QIntValidator()

        self.directory_path = None
        self.ftp_thread = None
        self.ftp_manager = FTPManager

        self.user, self.password, self.port = self.ui.input_user, self.ui.input_password, self.ui.input_port
        self.start_btn, self.stop_btn, self.path_btn = self.ui.btn_start, self.ui.btn_stop, self.ui.btn_path

        self.inputs = (self.user, self.password, self.port, self.start_btn, self.path_btn)
        self.setup_elements()

    def setup_elements(self):
        self.ui.label_user.setText('User')
        self.user.setText('admin')

        self.ui.label_password.setText('Password')
        self.password.setText('admin')

        self.ui.label_port.setText('Port')
        self.port.setValidator(self.onlyInt)
        self.port.setText('22')

        self.start_btn.setText('Start')
        self.start_btn.clicked.connect(self.start_server)

        self.stop_btn.setText('Stop')
        self.stop_btn.clicked.connect(self.stop_server)
        self.stop_btn.setDisabled(True)

        self.ui.address_box.setTitle('FTP address')
        self.ui.label_address.setText('')

        self.path_btn.setText('Set directory')
        self.path_btn.clicked.connect(self.path_button_action)
        self.ui.path_box.setTitle('Files path')
        self.ui.label_path.setText('')

    def path_button_action(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.directory_path = directory
        logger.info(f"current directory: {self.directory_path}")

    def start_server(self):
        import multiprocessing

        logger.info('started ftp server')
        self.ftp_thread = multiprocessing.Process(target=self.ftp_manager.start,
                                                  args=(self.user.text(), self.password.text(), self.port.text(),
                                                        self.directory_path))
        self.ftp_thread.start()
        self.disable_inputs()

        self.ui.label_address.setText(f'{self.ftp_manager.get_ip()}:{self.port.text()}')
        self.ui.label_path.setText(f'{self.ftp_manager.get_path(self.directory_path)}')

    def disable_inputs(self):
        for text_input in self.inputs:
            text_input.setDisabled(True)
        self.stop_btn.setDisabled(False)

    def enable_inputs(self):
        for text_input in self.inputs:
            text_input.setDisabled(False)
        self.stop_btn.setDisabled(True)

    def stop_server(self):
        logger.info('stopped ftp server')
        if self.ftp_thread:
            self.ftp_thread.terminate()
        self.enable_inputs()
        self.ui.label_address.setText('')


if __name__ == "__main__":
    multiprocessing.freeze_support()
    loader = QUiLoader()
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
