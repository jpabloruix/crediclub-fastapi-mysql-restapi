from datetime import date
from pydantic import BaseModel
from typing import Optional

class Credito(BaseModel):
    ID: Optional[str]
    PRIMER_NOMBRE: str
    APELLIDO_PAT: str
    APELLIDO_MAT: str
    FECHA_NAC: date
    RFC: Optional[str]
    INGRESOS_MENSUALES: float
    DEPENDIENTES: int
    APROBADO: Optional[str]
    
    