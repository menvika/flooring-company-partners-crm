# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'partner_cards.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_partner_cards(object):
    def setupUi(self, partner_cards):
        if not partner_cards.objectName():
            partner_cards.setObjectName(u"partner_cards")
        partner_cards.resize(608, 340)
        partner_cards.setStyleSheet(u"background-color: white;\n"
"color: black;")
        self.gridLayout = QGridLayout(partner_cards)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(partner_cards)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border: 1px solid black;\n"
"border-radius: 15px;\n"
"background-color:#F4E8D3; ")
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.button_name = QPushButton(self.frame)
        self.button_name.setObjectName(u"button_name")
        self.button_name.setStyleSheet(u"border:none;\n"
"font-size: 25px;\n"
"")

        self.verticalLayout.addWidget(self.button_name, 0, Qt.AlignmentFlag.AlignLeft)

        self.button_director = QPushButton(self.frame)
        self.button_director.setObjectName(u"button_director")
        self.button_director.setStyleSheet(u"border:none;\n"
"\n"
"font-size: 18px;")

        self.verticalLayout.addWidget(self.button_director, 0, Qt.AlignmentFlag.AlignLeft)

        self.button_phone = QPushButton(self.frame)
        self.button_phone.setObjectName(u"button_phone")
        self.button_phone.setMaximumSize(QSize(16777215, 200))
        self.button_phone.setStyleSheet(u"border:none;\n"
"\n"
"font-size: 18px;")

        self.verticalLayout.addWidget(self.button_phone, 0, Qt.AlignmentFlag.AlignLeft)

        self.button_rating = QPushButton(self.frame)
        self.button_rating.setObjectName(u"button_rating")
        self.button_rating.setStyleSheet(u"border:none;\n"
"\n"
"font-size: 18px;")

        self.verticalLayout.addWidget(self.button_rating, 0, Qt.AlignmentFlag.AlignLeft)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_sale = QLabel(self.frame)
        self.label_sale.setObjectName(u"label_sale")
        self.label_sale.setStyleSheet(u"border: none;\n"
"font-size: 40pt;\n"
"color: #67BA80;\n"
"font-weight: bold;\n"
"margin-left: 10pt;")

        self.verticalLayout_2.addWidget(self.label_sale, 0, Qt.AlignmentFlag.AlignRight)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button_see_sales_history = QPushButton(self.frame)
        self.button_see_sales_history.setObjectName(u"button_see_sales_history")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_see_sales_history.sizePolicy().hasHeightForWidth())
        self.button_see_sales_history.setSizePolicy(sizePolicy)
        self.button_see_sales_history.setMaximumSize(QSize(210, 30))
        self.button_see_sales_history.setStyleSheet(u"background-color:#67Ba80;\n"
"border-radius:15px;\n"
"margin-top: 5pt;\n"
"margin-left: 5pt;\n"
"margin-right: 5pt;\n"
"margin-bottom: 5pt;\n"
"border: none;\n"
"font-weight: bolder;\n"
"font-size: 18pt;\n"
"")

        self.horizontalLayout_3.addWidget(self.button_see_sales_history)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)


        self.retranslateUi(partner_cards)

        QMetaObject.connectSlotsByName(partner_cards)
    # setupUi

    def retranslateUi(self, partner_cards):
        partner_cards.setWindowTitle(QCoreApplication.translate("partner_cards", u"Form", None))
        self.button_name.setText(QCoreApplication.translate("partner_cards", u"PushButton", None))
        self.button_director.setText(QCoreApplication.translate("partner_cards", u"PushButton", None))
        self.button_phone.setText(QCoreApplication.translate("partner_cards", u"PushButton", None))
        self.button_rating.setText(QCoreApplication.translate("partner_cards", u"PushButton", None))
        self.label_sale.setText(QCoreApplication.translate("partner_cards", u"TextLabel", None))
        self.button_see_sales_history.setText(QCoreApplication.translate("partner_cards", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f \u043f\u0440\u043e\u0434\u0430\u0436", None))
    # retranslateUi

