from fastapi import APIRouter
from config.db import conn
from models.credito import creditos
from schemas.credito import Credito

credito = APIRouter()

@credito.post('/creditos')
def evaluar(credito: Credito):
    credito_nuevo = { 
                     "PRIMER_NOMBRE": credito.PRIMER_NOMBRE,
                     "APELLIDO_PAT": credito.APELLIDO_PAT,
                     "APELLIDO_MAT": credito.APELLIDO_MAT,
                     "FECHA_NAC": credito.FECHA_NAC,
                     "INGRESOS_MENSUALES": credito.INGRESOS_MENSUALES,
                     "DEPENDIENTES": credito.DEPENDIENTES
                    }
    credito_nuevo["RFC"] = get_rfc(credito)
    credito_nuevo["APROBADO"] = get_evaluacion(credito)
    
    result = conn.execute(creditos.insert().values(credito_nuevo))
    #result = conn.execute(creditos.select()).fetchall()
    #conn.execute(table('customers', column('company'), column('first_name'), column('last_name'), column('email'), column('phone')).insert().values({'company': 'sample name'}))
    print(result)
    
    respuesta = {
                    "id": result.lastrowid,
                    "rfc": credito_nuevo["RFC"],
                    "estatus": credito_nuevo["APROBADO"]
                }
    return respuesta

def get_rfc(credito: Credito):
    rfc = credito.APELLIDO_PAT.upper()[0:2]
    rfc += credito.APELLIDO_MAT.upper()[0:1]
    rfc += credito.PRIMER_NOMBRE.upper()[0:1]
    rfc += str(credito.FECHA_NAC.year)[2:4]
    rfc += str(credito.FECHA_NAC.month).rjust(2, '0')
    rfc += str(credito.FECHA_NAC.day).rjust(2, '0')
    
    return rfc

def get_evaluacion(credito: Credito):
    if credito.INGRESOS_MENSUALES > 25000:
        respuesta = "APROBADO"
    elif credito.INGRESOS_MENSUALES >= 15000 and credito.INGRESOS_MENSUALES <= 25000:
        if credito.DEPENDIENTES < 3:
            respuesta = "APROBADO"
        else:
            respuesta = "RECHAZADO"
    elif credito.INGRESOS_MENSUALES < 15000:
        respuesta = "RECHAZADO"
    
    return respuesta