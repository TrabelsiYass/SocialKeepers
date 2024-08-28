from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication
from ui_login import Ui_Form
from mainWindow_page import MainWindow_page
# from mainWindow_user import MainWindow_user
from splashPage_page import splashPage
from dbConnect import db


class login(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.WindowType.FramelessWindowHint)
        
        self.app = None
        self.USERNAME = "Nom de l'utilisateur"
        self.PASSWORD= "Mot de passe"
        self.userNameGroup = (self.login_lineEdit, self.groupBox_1, self.USERNAME)
        self.passsWordGroup = (self.pass_lineEdit, self.groupBox_2, self.PASSWORD)
        self.userNameLogin =""
        self.userPasswdLogin = ""
        print(self.userPasswdLogin)

        self.connect_btn.clicked.connect(self.connection)
        self.init()
    
    def connection(self):
             
        userNameLogin = self.userNameGroup[0].text()
        # username = self.userNameLogin
        # print(userNameLogin)
        userPasswdLogin = self.passsWordGroup[0].text()
        # print(userPasswdLogin)
        try:
            myCursor = db.cursor()
            myCursor.execute("select * from user where name = '"+userNameLogin+"' and passwrd = '"+userPasswdLogin+"' ")
            result = myCursor.fetchone()[0]
            print(result)
            if result == 1:
                self.msgLogin.setText("mot de passe et nom d'utilisateur correct !")
                self.msgLogin.setStyleSheet("color:green")
                self.msgLogin.setVisible(True)
                self.mainWindow = MainWindow_page()
                self.mainWindow.hide()
                self.splashPage = splashPage()
                self.close()
                self.splashPage.show()
                QtCore.QTimer().singleShot(2100,self.splashPage.hide)
                QtCore.QTimer().singleShot(2200,self.mainWindow.show)
            # elif result == 2:
            #     self.msgLogin.setText("mot de passe et nom d'utilisateur correct !")
            #     self.msgLogin.setStyleSheet("color:green")
            #     self.msgLogin.setVisible(True)
            #     self.mainWindow = MainWindow_user()
            #     self.mainWindow.hide()
            #     self.splashPage = splashPage()
            #     self.close()
            #     self.splashPage.show()
            #     QtCore.QTimer().singleShot(2100,self.splashPage.hide)
            #     QtCore.QTimer().singleShot(2200,self.mainWindow.show)
            # else:
            #     self.msgLogin.setVisible(True)
            #     self.msgLogin.setText("mot de passe ou nom d'utilisateur incorrect !")
            #     self.msgLogin.setStyleSheet("color:red")
        except Exception as e :
            self.msgLogin.setVisible(True)
            self.msgLogin.setText(f"connection db impossible !")
            self.msgLogin.setStyleSheet("color:red")
            print(e)


    def init(self):
        self.userNameGroup[1].setTitle("")
        self.passsWordGroup[1].setTitle("")
        self.msgLogin.setVisible(False)
        self.app = QApplication.instance()
        self.app.focusChanged.connect(self.updateComponent)

    def updateComponent(self, old_widget, now_widget):
        self.handel_focus_change(self.userNameGroup, old_widget, now_widget)
        self.handel_focus_change(self.passsWordGroup, old_widget, now_widget)

    @staticmethod
    def handel_focus_change(group, old_widget, now_widget):
        line_edit, group_box, title = group
        if old_widget == line_edit and line_edit.text().strip()== "":
            line_edit.setPlaceholderText(title)
            group_box.setTitle("")
        if now_widget == line_edit:
            line_edit.setPlaceholderText("")
            group_box.setTitle(title)


   
