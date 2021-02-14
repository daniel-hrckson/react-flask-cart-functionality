from collections import OrderedDict

def serialize_object(obj):
    return {
        "images": obj.images,
        "sku":obj.sku,
        "name":obj.name,
        "price":obj.price,
    }

def serialize_objects(list):
    dictionary = dict()
    for i in range(len(list)):
        dictionary.update({i: serialize_object(list[i])})
        
    return dictionary
