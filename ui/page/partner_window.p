# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'partner_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_partner_window(object):
    def setupUi(self, partner_window):
        if not partner_window.objectName():
            partner_window.setObjectName(u"partner_window")
        partner_window.resize(521, 404)
        partner_window.setStyleSheet(u"background-color:white;")
        self.gridLayout = QGridLayout(partner_window)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(partner_window)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(50, 50))
        self.label.setStyleSheet(u"background-color: none;")
        self.label.setPixmap(QPixmap(u"../icons/masterpol.ico"))
        self.label.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label)

        self.label_name = QLabel(partner_window)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setStyleSheet(u"font-size: 20pt;\n"
"background-color: none;\n"
"")

        self.horizontalLayout.addWidget(self.label_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_add = QPushButton(partner_window)
        self.button_add.setObjectName(u"button_add")
        self.button_add.setMinimumSize(QSize(200, 30))
        self.button_add.setStyleSheet(u"background-color:#67Ba80;\n"
"border-radius:15px;\n"
"margin-top: 5pt;\n"
"margin-left: 5pt;\n"
"margin-right: 5pt;\n"
"margin-bottom: 5pt;\n"
"border: none;\n"
"font-weight: bolder;\n"
"font-size: 18pt;\n"
"")

        self.verticalLayout_2.addWidget(self.button_add)

        self.button_exit = QPushButton(partner_window)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setMinimumSize(QSize(200, 30))
        self.button_exit.setStyleSheet(u"background-color:#67Ba80;\n"
"border-radius: 15px;\n"
"margin-top: 5pt;\n"
"margin-left: 5pt;\n"
"margin-right: 5pt;\n"
"margin-bottom: 5pt;\n"
"border: none;\n"
"font-weight: bolder;\n"
"font-size: 18pt;\n"
"")

        self.verticalLayout_2.addWidget(self.button_exit)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)

        self.scrollArea = QScrollArea(partner_window)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 495, 230))
        self.scrollAreaWidgetContents.setStyleSheet(u"border:none;\n"
"")
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)


        self.retranslateUi(partner_window)

        QMetaObject.connectSlotsByName(partner_window)
    # setupUi

    def retranslateUi(self, partner_window):
        partner_window.setWindowTitle(QCoreApplication.translate("partner_window", u"Form", None))
        self.label.setText("")
        self.label_name.setText(QCoreApplication.translate("partner_window", u"\u041f\u0430\u0440\u0442\u043d\u0435\u0440\u044b", None))
        self.button_add.setText(QCoreApplication.translate("partner_window", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u0430", None))
        self.button_exit.setText(QCoreApplication.translate("partner_window", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

