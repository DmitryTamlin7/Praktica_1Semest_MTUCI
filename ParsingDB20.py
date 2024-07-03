import requests
import pymysql
from ConfigDB import host, user, password, db_name

def get_vacancies(keyword):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": keyword,
        "area": 1,  # зона Москва
        "per_page": 20,  # Объектов на странице
    }
    headers = {
        "User-Agent": "Practica_MTUCI",
    }

    response = requests.get(url, params=params, headers=headers)  # запрос

    if response.status_code == 200:  # 200 - успех запроса
        data = response.json()
        vacancies = data.get("items", [])
        vacancy_list = []  # создаем список для хранения вакансий
        for vacancy in vacancies:
            # пишем значение которые нужно спарсить
            vacancy_title = vacancy.get('name')
            company_name = vacancy.get('employer', {}).get("name")
            vacancy_salary = vacancy.get('salary')
            if vacancy_salary:
                vacancy_salary_from = vacancy_salary.get("from")
                vacancy_salary_to = vacancy_salary.get("to")
                vacancy_salary_currency = vacancy_salary.get("currency")
            else:
                vacancy_salary_from = None
                vacancy_salary_to = None
                vacancy_salary_currency = None
                vacancy_url = vacancy.get('alternate_url')

            # добавляем вакансию в список
            vacancy_list.append({
                "vacancy_title": vacancy_title,
                "company_name": company_name,
                "vacancy_salary_from": vacancy_salary_from,
                "vacancy_salary_to": vacancy_salary_to,
                "vacancy_salary_currency": vacancy_salary_currency,
                "vacancy_url": vacancy_url
            })

        # добавляем вакансии в базу данных
        add_vacancies_to_db(vacancy_list)

    else:
        print(f"Request failed with status code: {response.status_code}")  # валидация ошибки и сообщение клиенту


def add_vacancies_to_db(vacancy_list):
    try:
        connection = pymysql.connect(
            host=host,
            port=3306,
            user=user,
            password=password,
            database=db_name,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("Connected!!!")
        print("#" * 20)

        try:
            with connection.cursor() as cursor:
                for vacancy in vacancy_list:
                    create_meaning = f"INSERT INTO parsingHH(vacancy_title, company_name, vacancy_salary_from, vacancy_salary_to, vacancy_salary_Currency, vacancy_url) VALUES('{vacancy['vacancy_title']}', '{vacancy['company_name']}', '{vacancy['vacancy_salary_from']}', '{vacancy['vacancy_salary_to']}', '{vacancy['vacancy_salary_currency']}', '{vacancy['vacancy_url']}');"
                    cursor.execute(create_meaning)
                connection.commit()
                print("Adding successful!")

            with connection.cursor() as cursor:
                select_all_rows = "SELECT * FROM parsingHH"
                cursor.execute(select_all_rows)
                rows = cursor.fetchall()
                for row in rows:
                    print(row)

        finally:
            connection.close()

    except Exception as ex:
        print("Connection failed!>>>>>>>")
        print(ex)


get_vacancies(input("Пожалуйста введите должность "))
