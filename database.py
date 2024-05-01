import pymongo
import certifi

URI = "mongodb+srv://alberthzaid2022:Zaid19@cluster0.dtmmy8t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
ca = certifi.where()
def connect():
    try:
        client = pymongo.MongoClient(URI, tlsCaFile=ca)
        db = client["Esteban"]
        print("Conexion exitosa")
    except ConnectionError:
        print('An error occurred')
    return db

