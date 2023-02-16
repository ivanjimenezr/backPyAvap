def compradorEntity(item) -> dict:
    return {
        "id": str(item['_id']),
        "nombre": item['nombre'],
        "dni": item['dni'],
        "direccion": item['direccion'],
        "municipio": item['municipio'],
        "provincia": item['provincia'],
        "email": item['email'],
        "telefono": item['telefono'],
        "fechaNacimiento": item['fechaNacimiento'],
        "estadoCivil": item['estadoCivil'],
        "fechaAlta": item['fechaAlta'],
        "finalizado": item['finalizado'],
    }
def compradoresEntity(entity) -> list:
    
    return[compradorEntity(item) for item in entity]