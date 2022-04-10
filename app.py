from HTMLElements import Examples

from sqlmodel import SQLModel, Session, select
from models import *
from db import engine

from datetime import datetime


def create_tables():
    # Whenerver classes inherit from SQLModel && cofigured with `table=True` they are registered in the `metadata` attribute
    SQLModel.metadata.create_all(engine) # creates all the tables

def create_rows():
    with Session(engine) as sesssion:
        team_one = Team(name="Preventers", headquarters="Sharp Tower")
        team_two = Team(name="T-Force", headquarters="La Fayette")
        sesssion.add(team_one) # adds row
        sesssion.add(team_two) # adds row
        sesssion.commit()

        hero_por = Hero(name="porcelain", team_id=team_one.id)
        hero_viagra = Hero(name="Viag-Man", age=1, team_id=team_two.id)

        sesssion.add(hero_por)
        sesssion.add(hero_viagra)
        sesssion.commit()

        sesssion.refresh(hero_por)
        sesssion.refresh(hero_viagra)
        
        print("Created hero: ", hero_por)
        print("Created hero: ", hero_viagra)

def select_heroes_and_their_teams():
    with Session(engine) as session:
        statement = select(Hero, Team).where(Hero.team_id == Team.id)
        results = session.exec(statement)
        for hero, team in results:
            print(f"Hero: {hero} | Team: {team}")

def select_heroes_joined_by_teams():
    with Session(engine) as session:
        statement = select(Hero, Team).join(Team, isouter=True) # + Hero's table outer left
        results = session.exec(statement)
        for hero, team in results:
            print(f"Hero: {hero} | Team: {team}")

def create_records():
    with Session(engine) as session:
        nationality1 = TypNarodnost(nazev="American")
        nationality2 = TypNarodnost(nazev="French")
        nationality3 = TypNarodnost(nazev="British")

        session.add_all(instances=[nationality1, nationality2, nationality3])
        session.commit()

        genre1 = TypZanr(nazev="Folk")
        genre2 = TypZanr(nazev="Indie")
        genre3 = TypZanr(nazev="Electro")

        session.add_all(instances=[genre1, genre2, genre3])

        song1 = Skladba(nazev="Dream Seam", delka=3)
        song2 = Skladba(nazev="Run to You", delka=2)
        song3 = Skladba(nazev="Mingle in Pine", delka=4)
        song4 = Skladba(nazev="Give Life Back to Music", delka=5)

        session.add_all(instances=[song1, song2, song3, song4])
        session.commit()

        album1 = Album(nazev="We Fall In", datum_vydani= datetime(2019,7,10), id_typ_zanr=genre1.id_typ_zanr)
        album2 = Album(nazev="Random Access Memory", datum_vydani=datetime(2013,5,17), id_typ_zanr=genre3.id_typ_zanr)
        album3 = Album(nazev="In That Room", datum_vydani=datetime(2020,1,6), id_typ_zanr=genre1.id_typ_zanr)

        session.add_all(instances=[album1, album2, album3])
        session.commit()

        artist1 = Interpret(nazev="Occie Elliot", id_typ_narodnost=nationality3.id_typ_narodnost)
        artist2 = Interpret(nazev="Daft Punk", id_typ_narodnost=nationality2.id_typ_narodnost)
        artist3 = Interpret(nazev="Imagine Dragons", id_typ_narodnost=nationality1.id_typ_narodnost)

        session.add_all(instances=[artist1, artist2, artist3])
        session.commit()

        ## album_interpret
        album_artist1 = AlbumInterpret(id_album=album1.id_album, id_interpret=artist1.id_interpret)
        album_artist2 = AlbumInterpret(id_album=album2.id_album, id_interpret=artist2.id_interpret)
        album_artist3 = AlbumInterpret(id_album=album3.id_album, id_interpret=artist1.id_interpret)

        session.add_all(instances=[album_artist1, album_artist2, album_artist3])


        ## album_skladba
        album_song1 = AlbumSkaldba(id_album=album1.id_album, id_skladba=song1.id_skladba, cislo_stopy=1)
        album_song2 = AlbumSkaldba(id_album=album1.id_album, id_skladba=song2.id_skladba, cislo_stopy=3)
        album_song3 = AlbumSkaldba(id_album=album1.id_album, id_skladba=song3.id_skladba, cislo_stopy=4)
        album_song4 = AlbumSkaldba(id_album=album2.id_album, id_skladba=song4.id_skladba, cislo_stopy=1)

        session.add_all(instances=[album_song1, album_song2, album_song3, album_song4])
        session.commit()



    
if __name__ == "__main__":
    
    ## print(Examples.simple_example())

    create_tables()
    # print(10*"--")
    # select_heroes_joined_by_teams()
    create_records()