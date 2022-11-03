from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:Pa$$w0rd@localhost:3306/creditosdb")

meta = MetaData()

conn = engine.connect()