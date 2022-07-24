import pymongo
client = pymongo.MongoClient("mongodb+srv://pratik:mongodb123@pratik.crzdz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={"name":"pratik","email":"pratil.941","surname":"thorat"}
db1=client['mongotest']
coll=db1['test1']
coll.insert_one(d)