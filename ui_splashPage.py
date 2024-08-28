# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashPage.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QProgressBar, QSizePolicy,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(632, 571)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(60, -1, -1, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/assets/icons/output-onlinepngtools.png"))

        self.verticalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.widget)

        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMaximumSize(QSize(16777215, 40))
        self.widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(94, 94, 94);\n"
"font: 700 8pt \"Segoe UI\";")

        self.verticalLayout.addWidget(self.label_2)

        self.progressBar_splash = QProgressBar(self.widget_2)
        self.progressBar_splash.setObjectName(u"progressBar_splash")
        self.progressBar_splash.setMaximumSize(QSize(16777215, 5))
        self.progressBar_splash.setStyleSheet(u"QProgressBar{\n"
"border-radius:10px;\n"
"	background-color: rgb(236, 234, 234);\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius: 10px;\n"
"	background-color: rgb(92, 124, 250);\n"
"}")
        self.progressBar_splash.setValue(0)
        self.progressBar_splash.setAlignment(Qt.AlignCenter)
        self.progressBar_splash.setTextVisible(False)

        self.verticalLayout.addWidget(self.progressBar_splash)


        self.verticalLayout_3.addWidget(self.widget_2)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Loading...", None))
    # retranslateUi

