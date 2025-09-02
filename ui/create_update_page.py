from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget, QMessageBox
from database.connection import SessionLocal
from database.init import session
from database.models.partners_model import partners_model
from ui.page.create_update import Ui_create_update

class create_partner(QWidget, Ui_create_update):

    session = SessionLocal()

    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller

        self.button_save.setText("Добавить нового партнера")
        self.label_name.setText("Добавление нового партнера")
        self.comboBox_type.addItems(["ПАО", "ЗАО", "ООО","ИП", "ОАО"])

        from app import main_window
        self.button_save.clicked.connect(self.save_partner) #обработка нажатия кнопки сохранить
        self.button_exit.clicked.connect(lambda: main_window.show_partners(controller)) #обработка нажатия кнопки назад

    def save_partner(self):
        # получение значений элементов со страницы
        name = self.lineEdit_name.text()
        type = self.comboBox_type.currentText()
        email = self.lineEdit_email.text()
        inn = self.lineEdit_inn.text()
        director = self.lineEdit_director.text()
        phone = self.lineEdit_phone.text()
        rating_str = self.lineEdit_rating.text()
        adres = self.lineEdit_address.text()

        try:
            #проверка корректности ввода
            if not name or not type or not email or not inn or not director or not phone or not rating_str:
                QMessageBox.critical(self,"Ошибка", "Все поля должны быть заполнены. Повторите ввод.")
                return

            if not '@' in email:
                QMessageBox.warning(self, 'Предупреждение', 'В адресе электронной почты должна быть "@". Повторите ввод.')
                return

            if not inn.isdigit():
                QMessageBox.warning(self, "Предупреждение", 'ИНН партнера должен быть числом')
                return

            if len(phone) != 13:
                QMessageBox.warning(self, 'Предупреждение', "Неверный формат номера. Введите номер в формате '999 999 99 99'")

            if '.' in rating_str  or ',' in rating_str:
                QMessageBox.warning(self, 'Предупреждение', 'Рейтинг должен быть целым числом. Повторите ввод.')
                return
            else:
                rating = int(rating_str)

            if rating < 0:
                QMessageBox.warning(self, 'Предупреждение', 'Рейтинг должен быть положительным числом. Повторите ввод.')
                return

            self.session.add(partners_model(name=name, type=type, email=email, inn=inn, director=director, phone=phone, rating=rating, address=adres))
            QMessageBox.information(self, "Информация", f'Данные о партнере {name} успешно добавлены!')
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            QMessageBox.critical(self, 'Ошибка', f'Ошибка добавления партнера {e}')


class update_partner(QWidget, Ui_create_update):

    session = SessionLocal()

    def __init__(self, controller, partner_id):
        super().__init__()
        self.setupUi(self)
        self.controller = controller

        for row in session.query(partners_model).filter(partners_model.id == partner_id).all():
            partner = row

        self.label_name.setText("Изменение партнера " + partner.name)
        self.button_save.setText("Сохранить изменения")
        self.comboBox_type.addItems(["ПАО", "ЗАО", "ООО","ИП", "ОАО"])
        self.lineEdit_name.setText(str(partner.name))
        self.lineEdit_inn.setText(str(partner.inn))
        self.lineEdit_email.setText(str(partner.email))
        self.lineEdit_phone.setText(str(partner.phone))
        self.comboBox_type.setCurrentText(str(partner.type))
        self.lineEdit_address.setText(str(partner.address))
        self.lineEdit_director.setText(str(partner.director))
        self.lineEdit_rating.setText(str(partner.rating))

        from app import main_window
        self.button_save.clicked.connect(lambda: self.save_partner(partner_id))
        self.button_exit.clicked.connect(lambda: main_window.show_partners(controller))

    def save_partner(self, partner_id):
        name = self.lineEdit_name.text()
        type = self.comboBox_type.currentText()
        email = self.lineEdit_email.text()
        inn = self.lineEdit_inn.text()
        director = self.lineEdit_director.text()
        phone = self.lineEdit_phone.text()
        rating_str = self.lineEdit_rating.text()
        adres = self.lineEdit_address.text()


        try:
            if not name or not type or not email or not inn or not director or not phone or not rating_str:
                QMessageBox.critical(self,"Ошибка", "Все поля должны быть заполнены. Повторите ввод.")
                return

            if not '@' in email:
                QMessageBox.warning(self, 'Предупреждение', 'В адресе электронной почты должна быть "@". Повторите ввод.')
                return

            if not inn.isdigit():
                QMessageBox.warning(self, "Предупреждение", 'ИНН партнера должен быть числом')
                return

            if len(phone) != 13:
                QMessageBox.warning(self, 'Предупреждение', "Неверный формат номера. Введите номер в формате '999 999 99 99'")

            if '.' in rating_str  or ',' in rating_str:
                QMessageBox.warning(self, 'Предупреждение', 'Рейтинг должен быть целым числом. Повторите ввод.')
                return
            else:
                rating = int(rating_str)

            if rating < 0:
                QMessageBox.warning(self, 'Предупреждение', 'Рейтинг должен быть положительным числом. Повторите ввод.')
                return

            partner_to_update = self.session.query(partners_model).filter_by(id=partner_id).first() # Находим партнера в базе данных по id

            if partner_to_update:
                # Обновляем данные
                partner_to_update.name = name
                partner_to_update.type = type
                partner_to_update.email = email
                partner_to_update.director = director
                partner_to_update.phone = phone
                partner_to_update.rating = rating
                partner_to_update.adres = adres

                # Сохраняем изменения
                self.session.commit()
                QMessageBox.information(self, "Информация", f'Данные о партнере {partner_to_update.name} успешно изменены!')
                self.session.commit()
        except Exception as e:
            session.rollback()
            QMessageBox.critical(self, 'Ошибка', f'Ошибка добавления партнера {e}')





