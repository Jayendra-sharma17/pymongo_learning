import pymongo

if __name__=="__main__":
    print("welcome to pymongo")
    client=pymongo.MongoClient("mongodb://localhost:27017")
    print(client)
    db=client['jayendra']
    collection=db['mysamplecollectionfor jayendra']
    # one=collection.find_one({'name':'jayendra'})
    # print(one)
    # find_all_name=collection.find({'name':'jayendra'})
    # for i in find_all_name:
    #     print(i)
    # alldocs=collection.find({'name':'jayendra'},{'name':0,'_id':1})
    # for item in alldocs:
    #     print(item)
    # alldocs=collection.find({'name':'jayendra'},{'Name':0}).limit(1)
    alldocs=collection.find({"name":"jayra","marks":{"$lte":80}})
    # print(collection.count_documents({}))
    # print(alldocs.count())f
    print(alldocs)
    for item in alldocs:
        print(item)
        print(item)