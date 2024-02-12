import pymongo

if __name__=="__main__":
    print("welcome to pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017")
    # print(client)
    db=client['jayendra']
    collection=db['mysamplecollectionfor jayendra']
    rec={"Name":"jay"}
    # collection.delete_one(rec)
    
    # up=collection.update_many(prev,nextt)
    # print(up.modified_count)

    up=collection.delete_many(rec)
    print(up.deleted_count)
   