SELECT alb.nazev AS album, inter.nazev AS artist
FROM album alb, album_skladba alb_sk, skladba sk, interpret inter, album_interpret alb_inter
WHERE alb.id_album = alb_sk.id_album
AND alb_sk.id_skladba = sk.id_skladba
AND alb.id_album = alb_inter.id_album
AND alb_inter.id_interpret = inter.id_interpret
AND sk.delka = (SELECT max(skladba.delka) FROM skladba)
LIMIT 1;