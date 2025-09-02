import sys
from PySide6.QtWidgets import QWidget
from database.init import session
from database.models.sales_history_model import sales_history_model
from ui.page.partner_cards import Ui_partner_cards
from ui.page.partner_window import Ui_partner_window
from database.models.partners_model import partners_model

class partner_page(QWidget, Ui_partner_window):
    def __init__(self, controller):
        super().__init__()
        self.setupUi(self)
        self.controller = controller
        self.fill_scroll_area()

        from app import main_window
        self.button_add.clicked.connect(lambda: main_window.show_create_page(controller)) ##обработка нажатия кнопки добавить
        self.button_exit.clicked.connect(lambda: sys.exit(0) )

    def fill_scroll_area(self):
        for partner in session.query(partners_model).order_by(partners_model.id).all():
            custom_widget = partner_card(self.controller, partner) #вызов функции длля получения карточек
            self.verticalLayout.addWidget(custom_widget)  #добавление карточек на страницу
        self.verticalLayout.update()

class partner_card(QWidget, Ui_partner_cards):
    def __init__(self, controller, partner):
        super().__init__()
        self.setupUi(self)
        self.controller = controller

        sale = count_sale(partner.id) #получение процента скидки

        # установка значений на карточку
        self.button_name.setText(str(partner.type) + " | " + str(partner.name))
        self.button_director.setText(str(partner.director))
        self.button_phone.setText("+7 " + str(partner.phone))
        self.button_rating.setText("Рейтинг: " + str(partner.rating))
        self.label_sale.setText(str(sale) + "%")

        from app import main_window
        self.button_see_sales_history.clicked.connect(lambda: main_window.show_sales_history(controller, partner.id)) #просмотр истории
        self.button_name.clicked.connect(lambda: main_window.show_update_page(controller, partner.id))
        self.button_phone.clicked.connect(lambda: main_window.show_update_page(controller, partner.id))
        self.button_rating.clicked.connect(lambda: main_window.show_update_page(controller, partner.id))
        self.button_director.clicked.connect(lambda: main_window.show_update_page(controller, partner.id))
        self.frame.mousePressEvent = lambda event, p=partner: main_window.show_update_page(controller, partner.id)


#вычисление скидки партнера
def count_sale(partner_id: int) -> int:
    sale = 0
    total_count = 0

    for order in session.query(sales_history_model).filter(sales_history_model.fk_partners_id == partner_id).all():
        total_count += order.count

    if 0 < total_count < 10000:
        sale = 0
    elif 10000 < total_count < 50000:
        sale = 5
    elif 50000 < total_count < 300000:
        sale = 10
    elif 300000 < total_count:
        sale = 15

    return sale
