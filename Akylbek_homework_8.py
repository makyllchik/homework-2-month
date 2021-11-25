import sqlite3

database = sqlite3.connect("user_work.db")
sql = database.cursor()


# sql.execute(
#     """
#     CREATE TABLE schedule(
#     name TEXT,
#     age INT
#     day TEXT,
#     time TEXT,
#     routine TEXT
#     )
#     """
# )
#
# database.commit()
def work():
    global name, age, day, time, routine
    name = input("Введите имя:")
    age = input("Введите ваш возраст:")
    day = input("Введите сколько дается дней на выполнение:")
    time = input("Введите время:")
    routine = input("Список дел:")

    sql.execute(f"SELECT routine FROM schedule WHERE routine = '{routine}' ")

    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO schedule VALUES (?,? ,?, ?, ?)", (name,age, day, time, routine))
        database.commit()
        print("Молодец, ты записал все дела, осталось только их выполнить")

    else:
        print("Уже есть такое")
        for value in sql.execute("SELECT*FROM schedule"):
            print(value)


work()
