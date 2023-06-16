import os
import sqlite3


def execute_query(query_sql: str) -> list:
    """
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    """
    db_pass = os.path.join(os.getcwd(), 'cards.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result


def unwrapper(records: list) -> None:
    """
    Функция для вывода результата выполнения запроса
    :param records: список ответа БД
    """
    for record in records:
        print(*record)
