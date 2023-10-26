import sqlite3


def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as e:
        print(e)


def create_product(connection, product: tuple):
    sql = '''
    INSERT INTO products 
    (product_title, price, quantity) 
    VALUES (?, ?, ?)
    '''
    try:
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as e:
        print(e)


def add_products(connection):
    products = [
        ('Dishwasher Detergent', 157.99, 20),
        ('Liquid soap with vanilla scent', 344.67, 15),
        ('Baby soap', 45.00, 35),
        ('Shampoo "Princess"', 267.99, 13),
        ('Shampoo "For Men"', 98.99, 17),
        ('Washing powder for white clothes"', 578.99, 25),
        ('Disposable Cups"', 5.49, 112),
        ('Disposable Plates"', 11.59, 80),
        ('Disposable Spoons and Forks"', 3.89, 102),
        ('Diapers"', 22.79, 200),
        ('Tooth Brush"', 132.79, 40),
        ('Tooth Paste"', 247.09, 20),
        ('Wet Wipes"', 89.13, 37),
        ('Paper Towels"', 102.77, 14),
        ('Floor Cleaner"', 256.02, 21),
    ]
    cursor = connection.cursor
    cursor.execute('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)
    connection.commit()


def update_products_quantity(connection, product_id, new_quantity):
    sql = '''UPDATE products SET quantity = ? WHERE id = ?'''
    cursor = connection.cursor
    cursor.execute(sql, (new_quantity, product_id))
    connection.commit()


def update_products_price(connection, product_id, new_price):
    sql = '''UPDATE products SET price = ? WHERE id = ?'''
    cursor = connection.cursor
    cursor.execute(sql, (new_price, product_id))
    connection.commit()


def delete_product(connection, product_id):
    cursor = connection.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id))
    connection.commit()


def select_all_products(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)


def select_affordable_products(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM products WHERE price < 100 AND quantity > 5')
    affordable_products = cursor.fetchall()
    for product in affordable_products:
        print(product)


def search_products_by_title(connection, title):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%' + title + '%',))
    matching_products = cursor.fetchall()
    for product in matching_products:
        print(product)


connection = create_connection('hw.db')

sql_create_products_table = '''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price DOUBLE(10,2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
    )
'''


if connection:
    print("Connection with DB is established")
    create_table(connection, sql_create_products_table)

add_products(connection)
update_products_quantity(connection, 1, 30)
update_products_price(connection, 2, 207.99)
delete_product(connection, 3)
select_all_products(connection)
select_affordable_products(connection)
search_products_by_title(connection, 'soap')


connection.close()
