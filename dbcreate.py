from pymongo import MongoClient
client = MongoClient('mongodb://test:test@localhost',27017)
db = client.jranking


db.users.insert_one({'id':'test01@gmail.com', 'password':'12345678', 'name':'테스트', 'classroom':'그린반', 'total':0, 'token':''})
db.times.insert_one({
    "id" : "QWE@NAV.COM",
    "date" : "2023-04-05",
    "start" : "21:09:03",
    "end" : "21:10:07"
})