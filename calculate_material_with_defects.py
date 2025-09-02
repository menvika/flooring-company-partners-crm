from math import ceil
from database.init import session
from database.models.material_type_model import material_type_model
from database.models.product_type_model import product_type_model


def calculate_material():

    try:
        product_type_id = int(input("Введите идентификатор типа продукции: "))
        material_type_id = int(input("Введите идентификатор типа материала: "))
        total = int(input("Введите количество продукции: "))
    except:
        print("Введено некорректное значение. Значение должно быть целым числом")
        return -1

    try:
        parametr1 = float(input("Введите первый параметр продукции (ширина в см): "))
        parametr2 = float(input("Введите второй параметр продукции (длина в см): "))
    except:
        print("Введено некорректное значение. Значение должно быть вещественным числом")
        return -1

    try:
        product_type = session.query(product_type_model).filter(product_type_model.id == product_type_id).first() #получение типа продукции по введенному id
        material_type = session.query(material_type_model).filter(material_type_model.id == material_type_id).first() #получение типа материала по введенному id

        material_not_defect = total * parametr1 * parametr2 * product_type.koef #расчет без учета брака
        itog_material = material_not_defect * (100 + material_type.defect)/100 #расчет с учетом брака
        print_itog_material = int(ceil(itog_material))

        print(f"Необходимо {print_itog_material} единиц материала.")
    except Exception:
        print("Не удалось найти материал или продукцию. Повторите ввод.")

if __name__ == "__main__":
    calculate_material()
