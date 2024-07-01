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

        with connection.cursor() as cursors:
            create_table_query = "CREATE TABLE parsing(id int auto_increment, Vacancy varchar(32), Company varchar(32), salary varchar(32), url varchar(52), primary key (id))"

                
            
            # Вакансия Компания salary :URL-адресс
            
            cursors.execute(create_table_query)
            print("Table created succesfully")
    finally:
        connection.close()
    
except Exception as ex: 
    print("Connect failed!>>>>>>>")
    print(ex)

