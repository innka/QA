import sqlite3
from datetime import date

class DataBase():#клас для БД

    def __init__(self):# кнструктор БД
        #Сутність щоб взаємодіяти з БД + шлях до БД
        self.connection = sqlite3.connect(r'C:\cygwin64\home\inka\QA\python_basic'
                                          + r'\become_qa_auto.db')
        self.cursor = self.connection.cursor()# стність що виконує команди в БД

    def test_connection(self):# метод з'єднання
        sqlite_select_Query = "SELECT sqlite_version();" # вивести версію БД
        self.cursor.execute(sqlite_select_Query)# виконання запиту в БД
        record = self.cursor.fetchall()# отримання результату виконання
        print(f"Connected successfully. SQLite DataBase Version is: {record}")
    
    #отримати усіх користувачів
    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    #отримати дані користувача за його іменем
    def get_all_user_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    #оновити дані продукту за id
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()#підтвердження змін в БД, щоб перевірити коректність роботи 

    #перед оновлення зробити виборку даних
    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_product_by_name(self, product_name):
        query = f"SELECT * FROM products WHERE name = {product_name}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    #додавання нових даних 
    def insert_product(self,product_id, name, descriptions, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES ({product_id}, '{name}', '{descriptions}', {qnt})"
        self.cursor.execute(query)
        self.connection.commit()#підтвердження змін в БД

    def delete_product_by_id(self, id_product):
        query = f"DELETE FROM products WHERE id = {id_product}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
                FROM orders \
                    JOIN customers ON orders.customer_id = customers.id\
                        JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    """
    individual project party
    """
    #отримати усі продукти
    def get_all_products(self):
        query = "SELECT * FROM products"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

       #отримати усі замовлення
    def get_all_orders(self):
        query = "SELECT * FROM orders"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def get_custumer_by_id(self, custumer_id):
        query = f"SELECT * FROM customers WHERE id = {custumer_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
        
    
    def insert_custumers(self,custumer_id, name, address, city, postal_code, country):
        if not isinstance(name, str) or not isinstance(address, str) or not isinstance(city, str) or not isinstance(postal_code, str) or not isinstance(country, str):
             raise ValueError("Invalid data type provided")
        else:
            query = f"INSERT OR REPLACE INTO customers (id, name, address, city, postalCode, country) \
                VALUES ({custumer_id}, '{name}', '{address}', '{city}', '{postal_code}', '{country}')"
            self.cursor.execute(query)
            self.connection.commit()#підтвердження змін в БД
    
    def update_custumers_name(self, custumer_id,name):
        if not isinstance(name, str) or name == "":
             raise ValueError("Invalid data type provided")
        else:
            query = f"UPDATE customers SET name = '{name}' WHERE id = {custumer_id}"
            self.cursor.execute(query)
            self.connection.commit()#підтвердження змін в БД, щоб перевірити коректність роботи 
    
    def update_custumers_address(self, custumer_id,address):
        if not isinstance(address, str) or address == "":
             raise ValueError("Invalid data type provided")
        else:
            query = f"UPDATE customers SET address = '{address}' WHERE id = {custumer_id}"
            self.cursor.execute(query)
            self.connection.commit()#підтвердження змін в БД, щоб перевірити коректність роботи 

    def update_custumers_city(self, custumer_id,city):
        if not isinstance(city, str) or city == "":
             raise ValueError("Invalid data type provided")
        else:
            query = f"UPDATE customers SET city = '{city}' WHERE id = {custumer_id}"
            self.cursor.execute(query)
            self.connection.commit()#підтвердження змін в БД, щоб перевірити коректність роботи 

    def update_custumers_postalCode(self, custumer_id,postalCode):
        if not isinstance(postalCode, str) or postalCode == "":
             raise ValueError("Invalid data type provided")
        else:
            query = f"UPDATE customers SET postalCode = '{postalCode}' WHERE id = {custumer_id}"
            self.cursor.execute(query)
            self.connection.commit()#підтвердження змін в БД, щоб перевірити коректність роботи 

    def update_custumers_country(self, custumer_id,country):
        if not isinstance(country, str) or country == "":
             raise ValueError("Invalid data type provided")
        else:
            query = f"UPDATE customers SET country = '{country}' WHERE id = {custumer_id}"
            self.cursor.execute(query)
            self.connection.commit()#підтвердження змін в БД, щоб перевірити коректність роботи 


    def delete_custumers_by_id(self, custumer_id):
        query = f"DELETE FROM customers WHERE id = {custumer_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_order_by_id(self, order_id):
        query = f"SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
                FROM orders \
                    JOIN customers ON orders.customer_id = customers.id\
                        JOIN products ON orders.product_id = products.id\
                            WHERE orders.id = {order_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def insert_new_order_2(self,order_id,customer_name, product_name, order_date):
        if  not isinstance(order_id, int) or not isinstance(customer_name, str) or not isinstance(product_name, str) or not isinstance(order_date, date):
            raise ValueError("Invalid data type provided")
        else:
            query = f"INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date)\
                VALUES ({order_id}, \
                (SELECT id FROM customers WHERE name = '{customer_name}'), \
                (SELECT id FROM products WHERE name = '{product_name}'), \
                {order_date})" 
            self.cursor.execute(query)
            self.connection.commit()#підтвердження змін в БД

    def insert_new_order(self,order_id,customer_id, product_id, order_date):
        if not isinstance(order_id, int) or not isinstance(customer_id, int) or not isinstance(product_id, int) or not isinstance(order_date, date):
            raise ValueError("Invalid data type provided")
        else:
            query = f"INSERT OR REPLACE INTO orders (id, customer_id, product_id, order_date) \
            VALUES ({order_id}, {customer_id}, {product_id}, {order_date})" 
            self.cursor.execute(query)
            self.connection.commit()#підтвердження змін в БД"""

    def update_orders_by_id_customer_name(self, order_id, customer_name):
        if not isinstance(order_id, int) or not isinstance(customer_name, str):
            raise ValueError("Invalid data type provided")
        else:
            query = f"UPDATE orders SET customer_id = (SELECT id FROM customers WHERE name = '{customer_name}') WHERE id = {order_id}"
            self.cursor.execute(query)
            self.connection.commit()#підтвердження змін в БД, щоб перевірити коректність роботи 
    
    def update_orders_by_id_product_name(self, order_id, product_name):
        if not isinstance(order_id, int) or not isinstance(product_name, str):
            raise ValueError("Invalid data type provided")
        else:
            query = f"UPDATE orders SET product_id = (SELECT id FROM products WHERE name = '{product_name}') WHERE id = {order_id}"
            self.cursor.execute(query)
            self.connection.commit()#підтвердження змін в БД, щоб перевірити коректність роботи 