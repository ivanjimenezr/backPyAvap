from typing import Optional,List
def inmuebleEntity(item) -> dict:
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
        # "dormitorios": item['dormitorios'],
        # "banos": item['banos'],
        # "exterior": item['exterior'],
        # "comisionVen": item['comisionVen'],
        # "comercial": item['comercial'],
        # "observaciones": item['observaciones'],
        # "comisionCom": item['comisionCom'],
        # "operacion": item['operacion'],
        # "cee": item['cee'],
        # "descripcion": item['descripcion'],
        # "ascensor": item['ascensor'],
        # "vendedores": List(item['vendedores'])

    }
def inmueblesEntity(entity) -> list:
    
    return[inmuebleEntity(item) for item in entity]