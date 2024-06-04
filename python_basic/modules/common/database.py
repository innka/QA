import sqlite3

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