from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime

## Assignment

class TypZanr(SQLModel, table=True): # genere type
    __tablename__ = "typ_zanr"

    id_typ_zanr: Optional[int] = Field(default=None, primary_key=True)
    nazev: str


class TypNarodnost(SQLModel, table=True): # nationality

    __tablename__ = "typ_narodnost"

    id_typ_narodnost: Optional[int] = Field(default=None, primary_key=True)
    nazev: str


class Skladba(SQLModel, table=True): # Composer
    id_skladba: Optional[int] = Field(default=None, primary_key=True)
    nazev: str
    delka: Optional[int]

    
class Album(SQLModel, table=True):
    id_album: Optional[int] = Field(default=None, primary_key=True)
    id_typ_zanr: Optional[int] = Field(default=None, foreign_key="typ_zanr.id_typ_zanr")
    nazev: str
    datum_vydani: datetime


class Interpret(SQLModel, table=True):
    id_interpret: Optional[int] = Field(default=None, primary_key=True)
    nazev: str
    id_typ_narodnost: Optional[int] = Field(default=None, foreign_key="typ_narodnost.id_typ_narodnost")


class AlbumInterpret(SQLModel, table=True):

    __tablename__ = "album_interpret"
    
    id_album_interpret: Optional[int] = Field(default=None, primary_key=True)
    id_album: Optional[int] = Field(default=None, foreign_key="album.id_album")
    id_interpret: Optional[int] = Field(default=None, foreign_key="interpret.id_interpret")

class AlbumSkaldba(SQLModel, table=True):
    
    __tablename__ = "album_skladba"

    id_album_skladba: Optional[int] = Field(default=None, primary_key=True)
    cislo_stopy: int
    id_album: Optional[int] = Field(default=None, foreign_key="album.id_album")
    id_skladba: Optional[int] = Field(default=None, foreign_key="skladba.id_skladba")

