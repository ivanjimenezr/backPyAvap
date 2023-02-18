def asociacionEntity(item) -> dict:
    return {
        "id": str(item['_id']),
        "idInmueble": item['idInmueble'],
        "idVendedor": item['idVendedor']
    }
def asociacionesEntity(entity) -> list:
    
    return[asociacionEntity(item) for item in entity]