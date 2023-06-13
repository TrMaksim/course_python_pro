import os
import sqlite3
from typing import List


def execute_query(query_sql: str) -> List:
    """
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    """
    db_pass = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_pass)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result


def unwrapper(records: List) -> None:
    """
    Функция для вывода результата выполнения запроса
    :param records: список ответа БД
    """
    for record in records:
        print(*record)


def output_of_profit() -> None:
    """
        Выводит общую сумму прибыли на основе
        цены за единицу и количества в таблице invoice_items.

        :return: None
    """
    query_sql = '''
        SELECT UnitPrice, Quantity
        FROM invoice_items;
    '''
    result = execute_query(query_sql)
    total_sum = sum(price * quantity for price, quantity in result)
    print(total_sum)


# output_of_profit()


def output_repeated_firstname() -> None:
    """
        Выводит повторяющиеся имена клиентов и количество повторений.

        :return: None
    """
    query_sql = '''
            SELECT FirstName
            FROM customers;
    '''
    result = execute_query(query_sql)
    first_name = [raw[0] for raw in result]

    counts = {}
    for name in first_name:
        counts[name] = counts.get(name, 0) + 1

    for name, count in counts.items():
        if count > 1:
            print(f'{name} | {count}')


# output_repeated_firstname()


def get_customers(state_name=None, city_name=None) -> List[str]:
    """
        Возвращает список клиентов на основе указанного штата и города.

        :param state_name: Название штата (по умолчанию None)
        :param city_name: Название города (по умолчанию None)
        :return: Список клиентов
        :rtype: List[str]
        """
    query_sql = '''
        SELECT FirstName
              ,City 
              ,State
          FROM customers
        '''
    filter_query = ''
    if city_name and state_name:
        filter_query = f" WHERE City = '{city_name}' and State = '{state_name}'"
    if city_name and not state_name:
        filter_query = f" WHERE City = '{city_name}'"
    if state_name and not city_name:
        filter_query = f" WHERE State = '{state_name}'"

    query_sql += filter_query
    result = execute_query(query_sql)
    customers = [raw[0] for raw in result]
    return customers
