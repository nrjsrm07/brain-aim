# from django.test import TestCase

# # Create your tests here.
from pymongo import MongoClient

mongo_uri = "mongodb+srv://nrjsrm07:asdfasdf@brainaimcluster.80z1pzq.mongodb.net/?retryWrites=true&w=majority&appName=BrainAimCluster"

client = MongoClient(mongo_uri)
print(mongo_uri)
# List the available databases
print(client.list_database_names())


# # Close the connection
# client.close()
