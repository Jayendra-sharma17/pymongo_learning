import pymongo

if __name__=="__main__":
    print("welcome to pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db=client['jayendra']
    collection=db['mysamplecollectionfor jayendra']
    dictionary={'name':'jayendra','marks':9988}
    collection.insert_one(dictionary)
    # insertThese=[
    #     {'_id':1,'Name':'jayendra','location':'kota','marks':34},
    #     {'_id':2,'Name':'jay','location':'china','marks':334},
    #     {'_id':3,'Name':'sharma','location':'ko ta','marks':346},
    #     {'_id':4,'Name':'jayra','location':'kota','marks':34}
    # ]
    # collection.insert_many(insertThese)

