# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sales_history.ui'
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

class Ui_sales_history(object):
    def setupUi(self, sales_history):
        if not sales_history.objectName():
            sales_history.setObjectName(u"sales_history")
        sales_history.resize(505, 389)
        sales_history.setStyleSheet(u"font: 18pt \"Arial\";\n"
"background-color: white;\n"
"color: black;")
        self.gridLayout = QGridLayout(sales_history)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(sales_history)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(50, 50))
        self.label_2.setStyleSheet(u"background-color:none;")
        self.label_2.setPixmap(QPixmap(u"ui/icons/masterpol.ico"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_name = QLabel(sales_history)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setStyleSheet(u"font-size: 30px;\n"
"background-color: none;")

        self.horizontalLayout.addWidget(self.label_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.scrollArea = QScrollArea(sales_history)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 479, 259))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_exit = QPushButton(sales_history)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setMinimumSize(QSize(200, 30))
        self.button_exit.setMaximumSize(QSize(16777215, 16777215))
        self.button_exit.setStyleSheet(u"background-color:#67Ba80;\n"
"border-radius: 15px;\n"
"border: none;\n"
"font-weight: bolder;\n"
"font-size: 18pt;\n"
"")

        self.verticalLayout_2.addWidget(self.button_exit)


        self.gridLayout.addLayout(self.verticalLayout_2, 2, 0, 1, 1)


        self.retranslateUi(sales_history)

        QMetaObject.connectSlotsByName(sales_history)
    # setupUi

    def retranslateUi(self, sales_history):
        sales_history.setWindowTitle(QCoreApplication.translate("sales_history", u"Form", None))
        self.label_2.setText("")
        self.label_name.setText(QCoreApplication.translate("sales_history", u"\u0417\u0430\u043a\u0430\u0437\u044b \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u0430", None))
        self.button_exit.setText(QCoreApplication.translate("sales_history", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

