# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(515, 399)
        Form.setStyleSheet(u"QWidget{\n"
"background-color:#F9F7F7;\n"
"}\n"
"\n"
"\n"
"#copyRight_widget{\n"
"background-color:#5C7CFA;\n"
"padding-right:4px;\n"
"padding-left:4px;\n"
"/*\n"
"border-bottom-left-radius:10px;\n"
"border-bottom-right-radius:10px;\n"
"border-top-left-radius:0px;\n"
"border-top-right-radius:0px;*/\n"
"\n"
"}\n"
"#copyRight_widget_label_2{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"padding-right:4px;\n"
"/*\n"
"border-bottom-right-radius:10px;\n"
"border-top-right-radius:none;\n"
"*/\n"
"}\n"
"#copyRight_widget_label_1{\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"padding-right:4px;\n"
"/*\n"
"border-bottom-left-radius:10px;\n"
"border-top-left-radius:0px;\n"
"*/\n"
"}\n"
"\n"
"\n"
"QGroupBox{\n"
"border-color: #5C7CFA;\n"
"border-style:solid;\n"
"border-width:1px;\n"
"margin-top:6px;\n"
"}\n"
"QGroupBox:title{\n"
"subcontrol-origin:margin;\n"
"left:10px;\n"
"bottom:5px;\n"
"padding: 0 5px;\n"
"}\n"
"QLineEdit{\n"
"border:none;\n"
"}\n"
"\n"
"\n"
"/*btn*/\n"
"\n"
"#annuler_btn {\n"
"background-co"
                        "lor:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}\n"
"#connect_btn {\n"
"background-color:#5C7CFA;\n"
"color:white;\n"
"border-radius: 5px;\n"
"border:none;\n"
"padding-right:8px;\n"
"padding-left:8px;\n"
"padding-top:2px;\n"
"padding-bottom:2px;\n"
"}\n"
"\n"
"#connect_btn:hover{\n"
"background-color:#7993F8;\n"
"color:#fbfafa;\n"
"}\n"
"#annuler_btn:hover{\n"
"background-color:#7993F8;\n"
"color:#fbfafa;\n"
"}\n"
"\n"
"#connect_btn:checked{\n"
"background-color:#3F72AF;\n"
"color:#112D4E;\n"
"}\n"
"#annuler_btn:checked{\n"
"background-color:#3F72AF;\n"
"color:#112D4E;\n"
"}\n"
"")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(2, 2, 2, 2)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setLayoutDirection(Qt.LeftToRight)
        self.widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"padding:4px;\n"
"}\n"
"\n"
"QPushButton{\n"
"border:none;\n"
"}\n"
"QLabel{\n"
"border:none;\n"
"}")
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(40, 2, 40, 2)
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font = QFont()
        font.setPointSize(9)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u":/assets/icons/output-onlinepngtools (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(40, 40))

        self.horizontalLayout_6.addWidget(self.pushButton_3)

        self.horizontalSpacer_3 = QSpacerItem(103, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u":/assets/icons/output-onlinepngtools (2).png"))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_4)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_3)

        self.copyRight_widget = QWidget(Form)
        self.copyRight_widget.setObjectName(u"copyRight_widget")
        self.copyRight_widget.setMinimumSize(QSize(0, 30))
        self.copyRight_widget.setMaximumSize(QSize(16777215, 30))
        self.horizontalLayout_5 = QHBoxLayout(self.copyRight_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.copyRight_widget_label_1 = QLabel(self.copyRight_widget)
        self.copyRight_widget_label_1.setObjectName(u"copyRight_widget_label_1")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Light"])
        font1.setPointSize(6)
        font1.setBold(True)
        self.copyRight_widget_label_1.setFont(font1)

        self.horizontalLayout_5.addWidget(self.copyRight_widget_label_1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.copyRight_widget_label_2 = QLabel(self.copyRight_widget)
        self.copyRight_widget_label_2.setObjectName(u"copyRight_widget_label_2")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI Light"])
        font2.setPointSize(7)
        font2.setBold(True)
        self.copyRight_widget_label_2.setFont(font2)
        self.copyRight_widget_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.copyRight_widget_label_2)


        self.verticalLayout.addWidget(self.copyRight_widget)


        self.gridLayout.addLayout(self.verticalLayout, 2, 0, 1, 1)

        self.mainLoginWidget = QWidget(Form)
        self.mainLoginWidget.setObjectName(u"mainLoginWidget")
        self.mainLoginWidget.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.verticalLayout_2 = QVBoxLayout(self.mainLoginWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, -1, 4, 10)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.line = QFrame(self.mainLoginWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line)

        self.label = QLabel(self.mainLoginWidget)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label.setFont(font3)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)

        self.line_2 = QFrame(self.mainLoginWidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_4.addWidget(self.line_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalSpacer_2 = QSpacerItem(20, 28, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.groupBox_1 = QGroupBox(self.mainLoginWidget)
        self.groupBox_1.setObjectName(u"groupBox_1")
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Semibold"])
        font4.setPointSize(12)
        self.groupBox_1.setFont(font4)
        self.horizontalLayout = QHBoxLayout(self.groupBox_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.login_lineEdit = QLineEdit(self.groupBox_1)
        self.login_lineEdit.setObjectName(u"login_lineEdit")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        self.login_lineEdit.setFont(font5)
        self.login_lineEdit.setFocusPolicy(Qt.ClickFocus)

        self.horizontalLayout.addWidget(self.login_lineEdit)


        self.verticalLayout_2.addWidget(self.groupBox_1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.groupBox_2 = QGroupBox(self.mainLoginWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font4)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pass_lineEdit = QLineEdit(self.groupBox_2)
        self.pass_lineEdit.setObjectName(u"pass_lineEdit")
        self.pass_lineEdit.setFont(font5)
        self.pass_lineEdit.setFocusPolicy(Qt.ClickFocus)
        self.pass_lineEdit.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.pass_lineEdit)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.msgLogin = QLabel(self.mainLoginWidget)
        self.msgLogin.setObjectName(u"msgLogin")
        self.msgLogin.setMinimumSize(QSize(0, 20))
        self.msgLogin.setStyleSheet(u"color: red;")
        self.msgLogin.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.msgLogin)

        self.verticalSpacer = QSpacerItem(20, 51, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.btn_widget = QWidget(self.mainLoginWidget)
        self.btn_widget.setObjectName(u"btn_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.btn_widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(40, -1, 40, -1)
        self.annuler_btn = QPushButton(self.btn_widget)
        self.annuler_btn.setObjectName(u"annuler_btn")
        self.annuler_btn.setLayoutDirection(Qt.RightToLeft)
        self.annuler_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(92, 124, 250);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(92, 124, 250);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/assets/icons/cancel-30.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u":/assets/icons/cancel-30+active.png", QSize(), QIcon.Normal, QIcon.On)
        self.annuler_btn.setIcon(icon1)
        self.annuler_btn.setCheckable(True)

        self.horizontalLayout_3.addWidget(self.annuler_btn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.connect_btn = QPushButton(self.btn_widget)
        self.connect_btn.setObjectName(u"connect_btn")
        self.connect_btn.setLayoutDirection(Qt.RightToLeft)
        self.connect_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(92, 124, 250);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(92, 124, 250);\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/assets/icons/connect-30.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u":/assets/icons/connect-30_active.png", QSize(), QIcon.Normal, QIcon.On)
        self.connect_btn.setIcon(icon2)
        self.connect_btn.setCheckable(False)

        self.horizontalLayout_3.addWidget(self.connect_btn)


        self.verticalLayout_2.addWidget(self.btn_widget)


        self.gridLayout.addWidget(self.mainLoginWidget, 1, 0, 1, 1)


        self.retranslateUi(Form)
        self.annuler_btn.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_3.setText("")
        self.label_4.setText("")
        self.copyRight_widget_label_1.setText(QCoreApplication.translate("Form", u"Azer Hasnaoui copyRight\u00a9", None))
        self.copyRight_widget_label_2.setText(QCoreApplication.translate("Form", u"2024", None))
        self.label.setText(QCoreApplication.translate("Form", u"Bienvenue", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("Form", u"Login", None))
        self.login_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Nom de l'utilisateur", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"mot de passe", None))
        self.pass_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Mot de passe", None))
        self.msgLogin.setText(QCoreApplication.translate("Form", u"mot de passe ou nom d'utilisateur incorrect !", None))
        self.annuler_btn.setText(QCoreApplication.translate("Form", u"Annuler    ", None))
        self.connect_btn.setText(QCoreApplication.translate("Form", u"Connecter    ", None))
    # retranslateUi

