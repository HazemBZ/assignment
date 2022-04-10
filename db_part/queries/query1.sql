select alb.nazev as album, art.nazev as artist, count(track) as nbr_tracks
from album alb, interpret art, skladba track, album_interpret album_artist, album_skladba
where alb.id_album = album_artist.id_album
and album_artist.id_interpret = art.id_interpret
and track.id_skladba = album_skladba.id_skladba
and album_skladba.id_album = alb.id_album
GROUP BY alb.nazev, art.nazev
ORDER BY alb.nazev, art.nazev;


