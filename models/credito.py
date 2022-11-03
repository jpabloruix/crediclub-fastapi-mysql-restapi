from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, Float, Boolean
from config.db import meta, engine

creditos = Table("creditos", meta, 
                 Column("ID", Integer, primary_key=True),
                 Column("PRIMER_NOMBRE", String(50)),
                 Column("APELLIDO_PAT", String(50)),
                 Column("APELLIDO_MAT", String(50)), 
                 Column("FECHA_NAC", Date),
                 Column("RFC", String(10)), 
                 Column("INGRESOS_MENSUALES", Float),
                 Column("DEPENDIENTES", Integer), 
                 Column("APROBADO", String(9)))

meta.create_all(engine)
