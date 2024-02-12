import pymongo

if __name__=="__main__":
    print("welcome to pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db=client['jayendra']
    collection=db['mysamplecollectionfor jayendra']
    prev={"Name":"jayendra"}
    nextt={'$set':{"location":"mumbaiiiii"}}
    # collection.update_one(prev,nextt)
    up=collection.update_many(prev,nextt)
    print(up.modified_count)
   