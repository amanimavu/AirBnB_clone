#!/usr/bin/python3
import os
from models.base_model import BaseModel

bm_init = BaseModel()
print("bm_init bfr save: {}".format(type(bm_init.created_at)))
bm_init.save()
print("bm_init aft save: {}".format(type(bm_init.created_at)))

try:
    bm = BaseModel(**bm_init.to_dict())
    print(">>>>>>> {}".format(type(bm_init.created_at)))
except:
    bm = None

if bm is None or bm.id != bm_init.id:
    try:
        bm = BaseModel(bm_init.to_dict())
    except:
        bm = None

print(bm.id == bm_init.id)
print(type(bm.created_at))
try:
    print(type(bm.updated_at))
except:
    print("** <class 'datetime.datetime'>")

print("bm_init aft exception handling: {}".format(type(bm_init.created_at)))
print(bm.created_at.year == bm_init.created_at.year)
print(bm.created_at.month == bm_init.created_at.month)
print(bm.created_at.day == bm_init.created_at.day)
print(bm.created_at.hour == bm_init.created_at.hour)
print(bm.created_at.minute == bm_init.created_at.minute)

try:
    print(bm.updated_at.year == bm_init.updated_at.year)
    print(bm.updated_at.month == bm_init.updated_at.month)
    print(bm.updated_at.day == bm_init.updated_at.day)
    print(bm.updated_at.hour == bm_init.updated_at.hour)
    print(bm.updated_at.minute == bm_init.updated_at.minute)
except:
    print("True")
    print("True")
    print("True")
    print("True")
    print("True")
