import sys 
from PySide6.QtWidgets import QApplication
from login_page import login
from mainWindow_page import MainWindow_page
# from mainWindow_user import MainWindow_user
from splashPage_page import splashPage
app = QApplication(sys.argv)
# window = login()
window = MainWindow_page()
# window = MainWindow_user()
window.show()
app.exec()