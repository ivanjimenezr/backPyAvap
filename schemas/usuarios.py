def usuarioEntity(item) -> dict:
    return {
        "id": str(item['_id']),
        "email": item['email'],
        "password": item['password']
    }
def usuariosEntity(entity) -> list:
    
    return[usuarioEntity(item) for item in entity]