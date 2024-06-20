import pytest
from modules.common.database import DataBase
from datetime import date
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

    """
    individual project party
    """
    """
    тести що вже є: оновити к-сть товару / додати новий товар / видалити продукт /
    """
@pytest.mark.idv_project5
def test_check_all_products():
    db = DataBase()
    products = db.get_all_products()
    #print("Продукти")
    #print(products)
    #print("\n")

@pytest.mark.idv_project5
def test_check_all_orders():
    db = DataBase()
    orders = db.get_all_orders()
    print("Замовленя")
    print(orders)
    print("\n")

@pytest.mark.idv_project5
def test_insert_costumers():
    db = DataBase()
    db.insert_custumers(99,"Andrii","Sobornosti 5", "Kyiv", "69007", "Ukraine")
    new_custumer = db.get_custumer_by_id(99)
    #print(new_custumer)
    assert new_custumer[0][0] == 99
    assert new_custumer[0][1] == "Andrii"
    assert new_custumer[0][2] == "Sobornosti 5"
    assert new_custumer[0][3] == "Kyiv"
    assert new_custumer[0][4] == "69007"
    assert new_custumer[0][5] == "Ukraine"

@pytest.mark.idv_project5
def test_update_name_custumer():
    db = DataBase()
    n_name = "Irina"#failed with n_name=123 and n_name=""
    db.update_custumers_name(99, n_name)
    new_name = db.get_custumer_by_id(99)# перевірка
    #print(new_name)
    assert new_name[0][0] == 99
    assert new_name[0][1] == n_name

@pytest.mark.idv_project5
def test_update_custumers_address():
    db = DataBase()
    n_address = "Mazepi 8" #failed with n_adress=123 and n_adress=""
    db.update_custumers_address(99,n_address)
    new_address = db.get_custumer_by_id(99)
    #print(new_address)
    assert new_address[0][0] == 99
    assert new_address[0][2] == n_address

@pytest.mark.idv_project5
def test_update_custumers_city():
    db = DataBase()
    n_city = "Yaremche" #failed with n_city=123 and n_city=""
    db.update_custumers_city(99,n_city)
    new_city = db.get_custumer_by_id(99)
    #print(new_city)
    assert new_city[0][0] == 99
    assert new_city[0][3] == n_city

@pytest.mark.idv_project5
def test_update_custumers_postalCode():
    db = DataBase()
    n_postalCode = "69001" #failed with n_postalCode=123 and n_postalCode=""
    db.update_custumers_postalCode(99,n_postalCode)
    new_postalCode = db.get_custumer_by_id(99)
    #print(new_postalCode)
    assert new_postalCode[0][0] == 99
    assert new_postalCode[0][4] == n_postalCode

@pytest.mark.idv_project5
def test_update_custumers_country():
    db = DataBase()
    n_country = "France" #failed with n_country=123 and n_country=""
    db.update_custumers_country(99,n_country)
    new_country = db.get_custumer_by_id(99)
    #print(new_country)
    assert new_country[0][0] == 99
    assert new_country[0][5] == n_country

@pytest.mark.idv_project5
def test_delete_custumers_by_id():
    db = DataBase()
    db.insert_custumers(999,"Andrii","Sobornosti 5", "Kyiv", "69007", "Ukraine")
    db.delete_custumers_by_id(999)
    del_custumer = db.get_custumer_by_id(999)
    assert len(del_custumer) == 0

@pytest.mark.idv_project5
def test_insert_new_order():
    db = DataBase()
    db.insert_new_order(99,2,3,date.today())
    new_order= db.get_detailed_order_by_id(99)
    #print(new_order)
    assert new_order[0][0] == 99
    

@pytest.mark.idv_project5
def test_insert_new_order_2():
    db = DataBase()
    db.insert_new_order_2(98,"Sergii","молоко",date.today())
    new_order= db.get_detailed_order_by_id(98)
    assert new_order[0][0] == 98
    assert new_order[0][1] == "Sergii"
    assert new_order[0][2] == "молоко"

@pytest.mark.idv_project5
def test_update_orders_by_id_customer_name():
    db = DataBase()
    n_name = "Stepan"
    db.update_orders_by_id_customer_name(98, n_name)
    new_order_customer = db.get_detailed_order_by_id(98)
    print(new_order_customer)
    assert new_order_customer[0][0] == 98
    assert new_order_customer[0][1] == n_name

@pytest.mark.idv_project5
def test_update_orders_by_id_product_name():
    db = DataBase()
    n_product = "круасан"
    db.update_orders_by_id_product_name(98, n_product)
    new_order_product = db.get_detailed_order_by_id(98)
    print(new_order_product)
    assert new_order_product[0][0] == 98
    assert new_order_product[0][2] == n_product 
    