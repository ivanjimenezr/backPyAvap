def inmuebleEntity(item) -> dict:
    return {
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
    }
def inmueblesEntity(entity) -> list:
    [inmuebleEntity(item) for item in entity]