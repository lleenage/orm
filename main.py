import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale

# from dotenv import load_dotenv
# import os.path


# dotenv_path = "confirm.env"
# if os.path.exists(dotenv_path):
#     load_dotenv(dotenv_path)

# login = os.getenv("LOGIN")
# password = os.getenv("PASSWORD")
# namedb = os.getenv("NAMEDB")


# DSN = f"postgresql://{login}:{password}@localhost:5432/{namedb}"
DSN = f"postgresql://postgres:2709200227092002@localhost:5432/netology_db"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

def get_shops(publ): #Функция принимает обязательный параметр
    qry = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale
            ).select_from(Shop).join(Stock.shop).join(Book.publisher).join(Publisher).join(Sale.stock).all()
    if publ.isdigit(): #Проверяем переданные данные в функцию на то, что строка состоит только из чисел
        qry = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale).session.query(qry).filter(Publisher.id == publ).all() #Обращаемся к запросу, который составили ранее, и применяем фильтрацию, где айди публициста равно переданным данным в функцию, и сохраняем в переменную
    else:
        qry = session.query(qry).filter(Publisher.name.like('%Пушкин %')).all() #Обращаемся к запросу, который составили ранее, и применяем фильтрацию, где имя публициста равно переданным данным в функцию, и сохраняем в переменную
    for b, sh, pr, d in qry: #Проходим в цикле по переменой, в которой сохраняем результат фильтрации, и при каждой итерации получаем кортеж и распаковываем значения в 4 переменные
        print(f"{b: <40} | {sh: <10} | {pr: <8} | {d.strftime('%d-%m-%Y')}") #Передаем в форматированную строку переменные, которые содержат имя книги, название магазина, стоимость продажи и дату продажи


if __name__ == '__main__':
    p_name = input("Введите имя или id автора: ") #Просим клиента ввести имя или айди публициста и данные сохраняем в переменную
    get_shops(p_name) #Вызываем функцию получения данных из базы, передавая в функцию данные, которые ввел пользователь строкой выше  





# # publisher_name = input('Введите имя автора: ')
# publisher_name = 'Александр Пушкин'
# publisher = Publisher(name=publisher_name)
# session.add(publisher)
# session.commit()
# # print(publisher)


# book1 = Book(title='Капитанская дочка', publisher_id='1')
# book2 = Book(title='Руслан и Людмила', publisher_id='1')
# book3 = Book(title='Евгений Онегин', publisher_id='1')
# session.add_all([book1, book2, book3])
# session.commit()
# # print(book1, book2, book3, sep='\n')


# shop1 = Shop(name='Буквоед')
# shop2 = Shop(name='Лабиринт')
# shop3 = Shop(name='Книжный дом')
# session.add_all([shop1, shop2, shop3])
# session.commit()
# # print(shop1, shop2, shop3, sep='\n')


# stock1 = Stock(book_id=1, shop_id=1, count=2)
# stock2 = Stock(book_id=1, shop_id=2, count=1)
# stock3 = Stock(book_id=2, shop_id=1, count=1)
# stock4 = Stock(book_id=3, shop_id=3, count=1)
# session.add_all([stock1, stock2, stock3, stock4])
# session.commit()
# # print(stock1, stock2, stock3, stock4, sep='\n')


# sale1 = Sale(price='600', date_sale='09-11-2022', stock_id='1', count='1')
# sale2 = Sale(price='600', date_sale='26-10-2022', stock_id='1', count='1')
# sale3 = Sale(price='500', date_sale='08-11-2022', stock_id='3', count='1')
# sale4 = Sale(price='580', date_sale='05-11-2022', stock_id='2', count='1')
# sale5 = Sale(price='490', date_sale='02-11-2022', stock_id='4', count='1')
# session.add_all([sale1, sale2, sale3, sale4, sale5])
# session.commit()
# # print(sale1, sale2, sale3, sale4, sale5, sep='\n')


# result = session.query(Book, Shop, Sale).filter(Publisher.name == publisher_name).filter(Publisher.id == Book.publisher_id).filter(Book.id == Stock.book_id).filter(Stock.shop_id == Shop.id).filter(Stock.id == Sale.stock_id).all()
# for r, c, k in result:
#     print(f'{r} {c} {c}')

session.close()