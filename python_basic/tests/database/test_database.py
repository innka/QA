import pytest
from modules.common.database import DataBase

@pytest.mark.database
def test_database_connection():
    db = DataBase()#екземпляр класу ДБ
    db.test_connection()# викнуємо метод підєднання

@pytest.mark.database
def test_check_all_users():
    db = DataBase()
    users = db.get_all_users()

    print(users)

@pytest.mark.database
def test_check_user_name():
    db = DataBase()
    user = db.get_all_user_by_name('Sergii')
    assert user[0][0] == 'Maydan Nezalezhnosti 1'
    assert user[0][1] == 'Kyiv'
    assert user[0][2] == '3127'
    assert user[0][3] =='Ukraine'

@pytest.mark.database
def test_product_qnt_update():
    db = DataBase()
    db.update_product_qnt_by_id(1,25)# нова к-сть товару
    water_qnt = db.select_product_qnt_by_id(1)# перевірка

    assert water_qnt [0][0] == 25

@pytest.mark.database
def test_product_insert():
    db = DataBase()
    db.insert_product(4,'печиво', 'солодке', 30)
    water_qnt = db.select_product_qnt_by_id(4)
    assert water_qnt[0][0] == 30

@pytest.mark.database
def test_product_delete():
    db = DataBase()
    db.insert_product(99,'test','test_data', 999)
    db.delete_product_by_id(99)
    qnt = db.select_product_qnt_by_id(99)
    assert len(qnt) == 0# довжина отриманого масиву = 0, тобто пустота
@pytest.mark.database
def test_detqiled_orders():
    db = DataBase()
    orders = db.get_detailed_orders()
    #перевірка вивду БД чисто для нас
    print("Замовлення ", orders)
    #первірка к-сті результатів
    assert len(orders) == 1
    #перевірка структури даних
    assert orders[0][0] == 1
    assert orders[0][1] == 'Sergii'
    assert orders[0][2] == 'солодка вода'
    assert orders[0][3] =='з цукром'