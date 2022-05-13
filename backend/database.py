import databases
import sqlalchemy


# DATABASE_URL = "postgresql://user:password@postgresserver/db"
DATABASE_URL = "postgresql://root:root@localhost/root"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

engine = sqlalchemy.create_engine(DATABASE_URL)
