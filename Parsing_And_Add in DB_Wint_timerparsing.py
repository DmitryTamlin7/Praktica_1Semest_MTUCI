import requests

def get_vacancies(keyword):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": keyword,
        "area": [],  # зона ALL
        "per_page": 1,  #Обьектов на странице
    }
    headers = {
        "User-Agent": "Practica_MTUCI", 
    }

    response = requests.get(url, params=params, headers=headers) #запрос

    if response.status_code == 200: # 200 - успех запроса
        data = response.json()
        vacancies = data.get("items", [])
        for vacancy in vacancies:
            # пишем значение которые нужно спарсить
            global vacancy_title
            global company_name       
            global vacancy_salary_from
            global vacancy_salary_to
            global vacancy_salary_currency
            global vacancy_url 
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
            
            print(f"Вакансия : {vacancy_title}\nКомпания : {company_name}\nsalary_from : {vacancy_salary_from}\nsalary_to : {vacancy_salary_to}\n Salary Curr : {vacancy_salary_currency}\nURL-адресс: {vacancy_url}\n")
            
    else:
        print(f"Request failed with status code: {response.status_code}") # валидация ошибки и сообщение клиенту



get_vacancies(input()) #запрос по вакансии 

import pymysql
from ConfigDB import host, user, password, db_name


try:
    connection = pymysql.connect(

        host=host,
        port = 3306,
        user = user,
        password= password,
        database= db_name,

        cursorclass = pymysql.cursors.DictCursor
    )
    print("Connected!!!")
    print("#" * 20)

    try:
                # create table
        # with connection.cursor() as cursors:
        #      create_table_query = "CREATE TABLE parsingHH(id int auto_increment, vacancy_title varchar(32), company_name varchar(32), vacancy_salary_from varchar(32) , vacancy_salary_to varchar(32), vacancy_salary_Currency varchar(52), vacancy_url varchar(52), primary key (id))"

        #         # Вакансия Компания salary :URL-адресс
            
        #      cursors.execute(create_table_query)
        #      print("Table created succesfully")

                # add meaning
          # таймер 15 сек на очищение таблицы
         with connection.cursor() as cursor:
            query = "CREATE EVENT delete_all_rows ON SCHEDULE EVERY 15 SECOND DO BEGIN DELETE FROM parsingHH; END"
            cursor.execute(query)
            # Запуск обработчика событий 
            cursor.execute("SET GLOBAL event_scheduler = ON")
            
        with connection.cursor() as cursors:
            create_meaning = f"INSERT INTO parsingHH(vacancy_title, company_name, vacancy_salary_from, vacancy_salary_to, vacancy_salary_Currency, vacancy_url) VALUES('{vacancy_title}', '{company_name}', '{vacancy_salary_from}', '{vacancy_salary_to}', '{vacancy_salary_currency}', '{vacancy_url}');"

            cursors.execute(create_meaning)
            connection.commit()

            print("adding succesfully!")

        




    finally:
        connection.close()
    
except Exception as ex: 
    print("Connect failed!>>>>>>>")
    print(ex)


print(vacancy_title, company_name, vacancy_salary_from, vacancy_salary_to, vacancy_salary_currency, vacancy_url)
