def inmuebleEntity(item) -> dict:
    print('ooo', item['provincia'])
    return {
        "id": str(item['_id']),
        "tipologia": item['tipologia'],
        "provincia": item['provincia'],
        "municipio": item['municipio'],
        "direccion": item['direccion'],
        "refCatastral": item['refCatastral'],
        "superficie": item['superficie'],
        "descripNotaSimple": item['descripNotaSimple'],
        "inscripcionRegistro": item['inscripcionRegistro'],
        "cru": item['cru'],
        "precio": item['precio'],
        "finalizado": item['finalizado'],
        "llaves": item['llaves'],
        "fechaAlta": item['fechaAlta'],
    }
def inmueblesEntity(entity) -> list:
    
    return[inmuebleEntity(item) for item in entity]