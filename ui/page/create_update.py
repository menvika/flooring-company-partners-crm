# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_update.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_create_update(object):
    def setupUi(self, create_update):
        if not create_update.objectName():
            create_update.setObjectName(u"create_update")
        create_update.resize(469, 467)
        create_update.setStyleSheet(u"font: \"Arial\";\n"
"	background-color: white;\n"
"	color: black;\n"
"\n"
"\n"
"")
        self.gridLayout = QGridLayout(create_update)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo = QLabel(create_update)
        self.logo.setObjectName(u"logo")
        self.logo.setMaximumSize(QSize(50, 50))
        self.logo.setStyleSheet(u"background-color:none;")
        self.logo.setPixmap(QPixmap(u"ui/icons/masterpol.ico"))
        self.logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.logo)

        self.label_name = QLabel(create_update)
        self.label_name.setObjectName(u"label_name")
        self.label_name.setMaximumSize(QSize(16777215, 40))
        self.label_name.setStyleSheet(u"background-color:none;\n"
"font-size: 30px;")

        self.horizontalLayout.addWidget(self.label_name)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.frame1 = QFrame(create_update)
        self.frame1.setObjectName(u"frame1")
        self.verticalLayout_2 = QVBoxLayout(self.frame1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.button_save = QPushButton(self.frame1)
        self.button_save.setObjectName(u"button_save")
        self.button_save.setMinimumSize(QSize(200, 30))
        self.button_save.setStyleSheet(u"background-color:#67Ba80;\n"
"border-radius: 15px;\n"
"margin-top: 5pt;\n"
"margin-left: 5pt;\n"
"margin-right: 5pt;\n"
"margin-bottom: 5pt;\n"
"border: none;\n"
"font-weight: bolder;\n"
"font-size: 18pt;\n"
"")

        self.verticalLayout_2.addWidget(self.button_save)

        self.button_exit = QPushButton(self.frame1)
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
"background-color:#67BA80;")

        self.verticalLayout_2.addWidget(self.button_exit)


        self.gridLayout.addWidget(self.frame1, 2, 0, 1, 1)

        self.frame = QFrame(create_update)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: white;\n"
"font-size: 15pt;\n"
"\n"
"QLineEdit {\n"
"border: 1px solid #F4E8D3;\n"
"font-size: 20px;\n"
"}\n"
"\n"
"QLabel {\n"
"font-size: 20px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_name_2 = QLabel(self.frame)
        self.label_name_2.setObjectName(u"label_name_2")
        self.label_name_2.setStyleSheet(u"font-size: 20px;\n"
"")

        self.horizontalLayout_5.addWidget(self.label_name_2)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_5.addItem(self.verticalSpacer_4)

        self.lineEdit_name = QLineEdit(self.frame)
        self.lineEdit_name.setObjectName(u"lineEdit_name")
        self.lineEdit_name.setStyleSheet(u"border: 2px solid #F4E8D3;\n"
"font-size: 20px;")

        self.horizontalLayout_5.addWidget(self.lineEdit_name)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_type = QLabel(self.frame)
        self.label_type.setObjectName(u"label_type")
        self.label_type.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_2.addWidget(self.label_type)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_2.addItem(self.verticalSpacer)

        self.comboBox_type = QComboBox(self.frame)
        self.comboBox_type.setObjectName(u"comboBox_type")
        self.comboBox_type.setStyleSheet(u"font-size: 20px;\n"
"border: 2px solid #F4E8D3;")

        self.horizontalLayout_2.addWidget(self.comboBox_type)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_email = QLabel(self.frame)
        self.label_email.setObjectName(u"label_email")
        self.label_email.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_8.addWidget(self.label_email)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_8.addItem(self.verticalSpacer_7)

        self.lineEdit_email = QLineEdit(self.frame)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setStyleSheet(u"font-size: 20px;\n"
"border: 2px solid #F4E8D3;")

        self.horizontalLayout_8.addWidget(self.lineEdit_email)


        self.verticalLayout.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_inn = QLabel(self.frame)
        self.label_inn.setObjectName(u"label_inn")
        self.label_inn.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_3.addWidget(self.label_inn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_3.addItem(self.verticalSpacer_2)

        self.lineEdit_inn = QLineEdit(self.frame)
        self.lineEdit_inn.setObjectName(u"lineEdit_inn")
        self.lineEdit_inn.setStyleSheet(u"font-size: 20px;\n"
"border: 2px solid #F4E8D3;")

        self.horizontalLayout_3.addWidget(self.lineEdit_inn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_director = QLabel(self.frame)
        self.label_director.setObjectName(u"label_director")
        self.label_director.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_6.addWidget(self.label_director)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_6.addItem(self.verticalSpacer_5)

        self.lineEdit_director = QLineEdit(self.frame)
        self.lineEdit_director.setObjectName(u"lineEdit_director")
        self.lineEdit_director.setStyleSheet(u"font-size: 20px;\n"
"border: 2px solid #F4E8D3;")

        self.horizontalLayout_6.addWidget(self.lineEdit_director)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_phone = QLabel(self.frame)
        self.label_phone.setObjectName(u"label_phone")
        self.label_phone.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_7.addWidget(self.label_phone)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_7.addItem(self.verticalSpacer_6)

        self.lineEdit_phone = QLineEdit(self.frame)
        self.lineEdit_phone.setObjectName(u"lineEdit_phone")
        self.lineEdit_phone.setStyleSheet(u"font-size: 20px;\n"
"border: 2px solid #F4E8D3;\n"
"")

        self.horizontalLayout_7.addWidget(self.lineEdit_phone)


        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_address = QLabel(self.frame)
        self.label_address.setObjectName(u"label_address")
        self.label_address.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_4.addWidget(self.label_address)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_4.addItem(self.verticalSpacer_3)

        self.lineEdit_address = QLineEdit(self.frame)
        self.lineEdit_address.setObjectName(u"lineEdit_address")
        self.lineEdit_address.setStyleSheet(u"font-size: 20px;\n"
"border: 2px solid #F4E8D3;")

        self.horizontalLayout_4.addWidget(self.lineEdit_address)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_rating = QLabel(self.frame)
        self.label_rating.setObjectName(u"label_rating")
        self.label_rating.setStyleSheet(u"font-size: 20px;")

        self.horizontalLayout_9.addWidget(self.label_rating)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.horizontalLayout_9.addItem(self.verticalSpacer_8)

        self.lineEdit_rating = QLineEdit(self.frame)
        self.lineEdit_rating.setObjectName(u"lineEdit_rating")
        self.lineEdit_rating.setStyleSheet(u"font-size: 20px;\n"
"border: 2px solid #F4E8D3;")

        self.horizontalLayout_9.addWidget(self.lineEdit_rating)


        self.verticalLayout.addLayout(self.horizontalLayout_9)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)


        self.retranslateUi(create_update)

        QMetaObject.connectSlotsByName(create_update)
    # setupUi

    def retranslateUi(self, create_update):
        create_update.setWindowTitle(QCoreApplication.translate("create_update", u"Form", None))
        self.logo.setText("")
        self.label_name.setText(QCoreApplication.translate("create_update", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c/\u0438\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u043f\u0430\u0440\u0442\u043d\u0435\u0440\u0430", None))
        self.button_save.setText(QCoreApplication.translate("create_update", u"PushButton", None))
        self.button_exit.setText(QCoreApplication.translate("create_update", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label_name_2.setText(QCoreApplication.translate("create_update", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438: ", None))
        self.label_type.setText(QCoreApplication.translate("create_update", u"\u0422\u0438\u043f \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438:", None))
        self.label_email.setText(QCoreApplication.translate("create_update", u"\u0410\u0434\u0440\u0435\u0441 \u044d\u043b. \u043f\u043e\u0447\u0442\u044b:", None))
        self.label_inn.setText(QCoreApplication.translate("create_update", u"\u0418\u041d\u041d: ", None))
        self.label_director.setText(QCoreApplication.translate("create_update", u"\u0418\u043c\u044f \u0434\u0438\u0440\u0435\u043a\u0442\u043e\u0440\u0430:", None))
        self.label_phone.setText(QCoreApplication.translate("create_update", u"\u041d\u043e\u043c\u0435\u0440 \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0430:", None))
        self.label_address.setText(QCoreApplication.translate("create_update", u"\u042e\u0440. \u0430\u0434\u0440\u0435\u0441:", None))
        self.label_rating.setText(QCoreApplication.translate("create_update", u"\u0420\u0435\u0439\u0442\u0438\u043d\u0433:", None))
    # retranslateUi

