#!/usr/bin/python3
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

#### This block of code below is setUp #########################

fs = FileStorage() #create a file storage object
file_path = "file.json" #define the file_path
try:
    file_path = FileStorage._FileStorage__file_path #assign the variable file path the value for __file_path attribute
except:
    pass
try:
    os.remove(file_path) #delete the file used to save data after deserialization
except:
    pass
try:
    fs._FileStorage__objects.clear() #delete elements in the __objects dictionary
except:
    pass

#################################################################

ids = [] #define a list called ids to store ids of objects
objs_by_id = {} #define a dictionary to store objects mapped with their ids
for i in range(10):
    bm = BaseModel() #create a BaseModel instance
    fs.new(bm) #include the newly created BaseModel instance in the dictionary __objects
    bm.save() #serialize the __objects dictionary and store in file defined by file_path
    ids.append(bm.id) #store the newly created BaseModel's id in an array
    objs_by_id[bm.id] = bm #store the newly created BaseModel object in a dictionary mapping it with its id

try:
    fs._FileStorage__objects.clear() #delete elements in the __objects dictionary
except:
    pass
fs.reload() #deserialize the JSON string contained in the file given by filepath and store the objects in the __objects dictionary

all_reloaded = fs.all() #return the dictionary(__objects) containing all the instances we have gotten from the file given by file_path

if len(all_reloaded.keys()) != len(ids):
    print("Missing after reload") #confirm the all instances that were created had been saved and have the reloaded back

for id in ids: #loop through the ids list
    if all_reloaded.get(id) is None and all_reloaded.get("{}.{}".format("BaseModel", id)) is None: #check if there is any key in all_realoaded that is None
        print("Missing {}".format(id))

for id in ids: #loop through the ids list
    obj_reloaded = all_reloaded.get(id)
    if obj_reloaded is None:
        obj_reloaded = all_reloaded.get("{}.{}".format("BaseModel", id))
    print(obj_reloaded.__class__.__name__)
    obj_created = objs_by_id[id]
    print(obj_reloaded.id == obj_created.id)
    print(obj_reloaded.created_at == obj_created.created_at)
    print(obj_reloaded.updated_at == obj_created.updated_at)

try:
    os.remove(file_path)
except Exception as e:
    pass
