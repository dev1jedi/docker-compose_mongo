import pymongo

# Подключение к MongoDB
client = pymongo.MongoClient("mongodb://mongo:27017/")
db = client["mydatabase"]
collection = db["mycollection"]

# Добавление документа в коллекцию
post = {"title": "Пример заголовка", "content": "Пример контента"}
collection.insert_one(post)

# Вывод всех документов из коллекции
for post in collection.find():
    print(post)
