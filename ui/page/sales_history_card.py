# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sales_history_card.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_sales_history_cards(object):
    def setupUi(self, sales_history_cards):
        if not sales_history_cards.objectName():
            sales_history_cards.setObjectName(u"sales_history_cards")
        sales_history_cards.resize(400, 300)
        sales_history_cards.setStyleSheet(u"font: 18pt \"Arial\";\n"
"background-color: white;\n"
"color: black;\n"
"")
        self.gridLayout = QGridLayout(sales_history_cards)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(sales_history_cards)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border: 2px solid #F4E8D3;\n"
"border-radius: 15px;\n"
"background-color: white;")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_name = QLabel(self.frame)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setStyleSheet(u"border: none;\n"
"font-size: 20pt;")

        self.verticalLayout.addWidget(self.label_name)

        self.label_count = QLabel(self.frame)
        self.label_count.setObjectName(u"label_count")
        self.label_count.setStyleSheet(u"border: none;\n"
"font-size: 20pt;\n"
"")

        self.verticalLayout.addWidget(self.label_count)

        self.label_date = QLabel(self.frame)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setStyleSheet(u"border: none;\n"
"font-size: 20pt;")

        self.verticalLayout.addWidget(self.label_date)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(sales_history_cards)

        QMetaObject.connectSlotsByName(sales_history_cards)
    # setupUi

    def retranslateUi(self, sales_history_cards):
        sales_history_cards.setWindowTitle(QCoreApplication.translate("sales_history_cards", u"Form", None))
        self.label_name.setText(QCoreApplication.translate("sales_history_cards", u"TextLabel", None))
        self.label_count.setText(QCoreApplication.translate("sales_history_cards", u"TextLabel", None))
        self.label_date.setText(QCoreApplication.translate("sales_history_cards", u"TextLabel", None))
    # retranslateUi

