from common.database import Database

Database.initialize()
Database.insert('users',{"account":"kevin@test.com","password":"123456","name":"kevin"})
user = Database.find_one('users',{"account":"kevin@test.com"})
print(user)