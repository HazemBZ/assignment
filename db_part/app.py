
from sqlmodel import SQLModel, text
from models import *
from db import DBManager






    
if __name__ == "__main__":
    
    ## Run once
    # DBManager.create_tables() 
    # DBManager.create_records() 

    ## Queries
    DBManager.exec_query1()
    DBManager.exec_query2()