def serialize_object(obj):
    return {
        "sku":obj.sku,
        "name":obj.name,
        "price":obj.price,
        "images": obj.images,
    }

def serialize_objects(list):
    dictionary = dict()
    for i in range(len(list)):
        dictionary.update({i: serialize_object(list[i])})
    return dictionary
