## Учебная Практика - Платформа Парсинга данных о соискателях и вакансиях

## Цель работы
Разработка платформы для парсинга данных о соискателях и вакансиях с платформы hh.ru.

## Задачи
1) Изучить существующие платформы для парсинга (beautiful soap, selenium или API платформ);
2) Сформулировать функциональные требования к системе;
3) Спроектировать базу данных;
4) Написать инструкцию пользователя;
5) Провести тестирование системы.

## Функционал
1) Возможность формирования запроса для парсинга данных по таким полям, как ФИО, название должности, навыки, формат работы и т.д.
2) Загрузка в базу данных информации по результатам парсинга и вывод аналитики по параметрам (например, сколько есть вакансий и сколько кандидатов на вакансию).

## Требования к frontend
Может быть реализован в качестве веб-интерфейса на любом стеке технологий (например, фреймворк Django). Также в качестве интерфейса взаимодействия с клиентом может быть реализован телеграм-бот.

## Требования к backend
Язык программирования: Python.
База данных: MySQL, PostgreSQL, MongoDB.
Каждый сервис должен быть упакован в отдельный Docker-контейнер.

## Запуск
Вся система должна подниматься посредством docker-compose.


##Educational Practice - Data Parsing Platform for Job Applicants and Vacancies

## Goal
Development of a platform for parsing data on job applicants and vacancies from the hh.ru platform.

## Tasks
1) Study existing platforms for parsing (beautiful soap, selenium, or platform APIs);
2) Formulate functional requirements for the system;
3) Design the database;
4) Write user instructions;
5) Conduct system testing.

## Functionality
1) Ability to create a request for parsing data based on fields such as full name, job title, skills, work format, etc.
2) Loading parsed information into the database and displaying analytics on parameters (for example, the number of vacancies and the number of candidates per vacancy).

## Frontend requirements
Can be implemented as a web interface using any technology stack (e.g. Django framework). An interface for interacting with the client can also be implemented as a Telegram bot.

## Backend requirements
Programming language: Python.
Database: MySQL, PostgreSQL, MongoDB.
Each service should be packaged in a separate Docker container.

## Launch
The entire system should be started using docker-compose.
