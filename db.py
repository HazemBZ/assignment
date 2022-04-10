from sqlmodel import create_engine

db_name = '' # defaults to postgres
db_url = f"postgresql+psycopg2://postgres:@localhost/{db_name}"


engine = create_engine(db_url, echo=True) # echo 'True' will make engine print all the SQL statements it executes
