from PySide6.QtWidgets import  QWidget
from database.init import session
from database.models.partners_model import partners_model
from database.models.products_model import product_model
from database.models.sales_history_model import sales_history_model
from ui.page.sales_history import Ui_sales_history
from ui.page.sales_history_card import Ui_sales_history_cards

class sales_history(QWidget, Ui_sales_history):
    def __init__(self, controller, partner_id):
        super().__init__()
        self.setupUi(self)
        self.controller = controller

        from app import main_window
        self.button_exit.clicked.connect(lambda: main_window.show_partners(controller) )

        for partner in session.query(partners_model).filter(partners_model.id == partner_id).all(): #получение текущего партнера
            self.label_name.setText("История продаж партнера ''" + str(partner.name) + "'':")

        for order in session.query(sales_history_model).filter(sales_history_model.fk_partners_id == partner_id).all(): #получение всех заказов партнера
            custom_widget = sales_history_card(order)
            self.verticalLayout.addWidget(custom_widget)
        self.verticalLayout.update()

class sales_history_card(QWidget, Ui_sales_history_cards):
    def __init__(self, order):
        super().__init__()
        self.setupUi(self)

        product_name = session.query(product_model.name).filter(product_model.id == order.fk_products_id).scalar() #получение наименования продукции по вторичному ключу
        self.label_name.setText("Название: " + str(product_name))
        self.label_count.setText("Количество: " + str(order.count))
        self.label_date.setText("Дата продажи: " + str(order.date))

