from sqlmodel import create_engine, SQLModel, Session

sqlite_file_name = "/media/giuff/Windows-SSD/Users/gffpl/Lab_2026/app/data/database.db"    #posizione del file in memoria
sqlite_url = f"sqlite:///{sqlite_file_name}"    #endpoint dove viene montato a runtime
engine = create_engine(
    sqlite_url,
    connect_args={"check_same_thread": False},
    echo=True
    ) #creazione del motore di connessione al database

def init_database():
    SQLModel.metadata.create_all(engine)    #creazione del database se non esiste già