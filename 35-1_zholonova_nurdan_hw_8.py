import sqlite3

connection = sqlite3.connect('company.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    )
''')

cursor.execute("INSERT INTO countries (title) VALUES ('Kyrgyzstan')")
cursor.execute("INSERT INTO countries (title) VALUES ('Canada')")
cursor.execute("INSERT INTO countries (title) VALUES ('Italy')")

cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Bishkek', 127, 1)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Osh', 88, 1)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Ottawa', 2790, 2)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Toronto', 630, 2)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Vancouver', 115, 2)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Rome', 1285, 3)")
cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Milan', 181.8, 3)")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id)
    )
''')

cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Aidana', 'Atabekova', 2)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Emirhan', 'Dzhumabaev', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Elkhan', 'Sultanov', 1)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Ethan', 'Mitchel', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Lucas', 'Wilson', 4)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Adrian', 'Agrest', 3)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Olivia', 'Smith', 5)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Anjelina', 'Williams', 5)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Lien', 'Johnson', 5)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Sophia', 'Anderson', 4)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Isabella', 'Morette', 7)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Luca', 'Fernando', 7)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Giovanni', 'Rossi', 6)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Marco', 'Bianchi', 6)")
cursor.execute("INSERT INTO employees (first_name, last_name, city_id) VALUES ('Sophia', 'Martiani', 7)")

connection.commit()
connection.close()

while True:
    print("You can display a list of employees by selecting a city "
          "ID from the list of cities below; to exit the program, enter 0:")
    connection = sqlite3.connect('company.db')
    cursor = connection.cursor()
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    for city in cities:
        print(f"{city[0]}. {city[1]}")
    connection.close()
    selected_city_id = input("Enter city id (or 0 to exit): ")
    if selected_city_id == "0":
        print("The program has ended.")
        break
    try:
        selected_city_id = int(selected_city_id)
        connection = sqlite3.connect('company.db')
        cursor = connection.cursor()
        cursor.execute("SELECT e.first_name, e.last_name, countries.title, c.title,"
                       " c.area FROM employees e " "JOIN cities c ON e.city_id = c.id " 
                       "JOIN countries ON c.country_id = countries.id "
                       "WHERE e.city_id = ?", (selected_city_id,))
        employees = cursor.fetchall()
        connection.close()
        if employees:
            print("Employees living in the selected city:")
            for employee in employees:
                print(f"First Name: {employee[0]}, Last Name: {employee[1]}, Country:"
                      f" {employee[2]}, City: {employee[3]}, City Area: {employee[4]} km")
        else:
            print("There are no employees in the selected city.")
    except ValueError:
        print("Enter the correct city id.")
