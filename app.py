import sys
from PySide6.QtCore import QTranslator, QLibraryInfo
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget
from ui.create_update_page import create_partner, update_partner
from ui.partner_page import partner_page
from ui.sales_history_page import sales_history

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("МастерПол")
        self.setGeometry(400, 200, 700, 500) #отступ от левого верхнего угла и размеры окна

        self.central_widget = QStackedWidget()
        self.setCentralWidget(self.central_widget)
        self.partner_page = partner_page(self)
        self.central_widget.addWidget(self.partner_page)
        self.second_page = None

    def show_sales_history(self, partner_id:int): #отображение истории продаж
        self.setWindowTitle("МастерПол")
        self.second_page = sales_history(self, partner_id)
        self.central_widget.addWidget(self.second_page)
        self.central_widget.setCurrentWidget(self.second_page)

    def show_partners(self): #отображение начальной страницы партнеров
        self.setWindowTitle("МастерПол")
        self.second_page = partner_page(self)
        self.central_widget.addWidget(self.second_page)
        self.central_widget.setCurrentWidget(self.second_page)

    def show_create_page(self): #отображение страницы добавления партнера
        self.setWindowTitle("МастерПол")
        self.second_page = create_partner(self)
        self.central_widget.addWidget(self.second_page)
        self.central_widget.setCurrentWidget(self.second_page)

    def show_update_page(self, partner_id): #отображение страницы изменения партнера
        self.setWindowTitle("МастерПол")
        self.second_page = update_partner(self, partner_id)
        self.central_widget.addWidget(self.second_page)
        self.central_widget.setCurrentWidget(self.second_page)

if __name__ == "__main__":
    app = QApplication(sys.argv) # создание приложения
    window = main_window() # создание главного окна приложения
    window.setWindowIcon(QPixmap("ui/icons/masterpol.ico")) # иконка приложения
    window.show() # отображение главного окна
    app.exec() # запуск цикла обработки событий приложения