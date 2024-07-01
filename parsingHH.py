import requests

def get_vacancies(keyword):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": keyword,
        "area": [],  # зона ALL
        "per_page": 20,  #Обьектов на странице
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
            vacancy_title = vacancy.get("name")
            company_name = vacancy.get("employer", {}).get("name")
            vacancy_salary = vacancy.get("salary")
            vacancy_url = vacancy.get("alternate_url")
            print(f"Вакансия : {vacancy_title}\nКомпания : {company_name}\nSalary : {vacancy_salary}\nURL-адресс: {vacancy_url}\n")
    else:
        print(f"Request failed with status code: {response.status_code}") # валидация ошибки и сообщение клиенту



get_vacancies("Java") #запрос по вакансии 

