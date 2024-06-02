Domanda 1)

SELECT v.comp, avg(durataminuti) as durata_media 
FROM arrpart, aeroporto ap, luogoaeroporto l, Volo v
WHERE arrpart.partenza=ap.codice
AND l.aeroporto=ap.codice
AND arrpart.codice = v.codice
AND nazione = 'Italy'
GROUP BY v.comp
ORDER BY durata_media ASC;
-----------------------------------------------------

Domanda 2)

SELECT DISTINCT comp 
FROM Volo v
WHERE durataminuti > (SELECT avg(durataminuti) FROM volo);
-----------------------------------------------------

Domanda 3)


-----------------------------------------------------

Domanda 4)


-----------------------------------------------------

Domanda 5)


-----------------------------------------------------

Domanda 6)


-----------------------------------------------------