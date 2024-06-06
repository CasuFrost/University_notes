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

WITH MediaDurataVolo as 
(SELECT avg(durataminuti) as durata_media FROM volo),
	
WITH MediaDurataCompagnia as (SELECT comp,avg(durataminuti) as media_durata 
FROM Volo 
GROUP BY comp)

SELECT  *
FROM MediaDurataCompagnia as mdc,MediaDurataVolo as mdv
WHERE mdc.media_durata>mdv.durata_media
-----------------------------------------------------

Domanda 3)

-- conteggio per ogni città 
with conteggioArriviPerCitta as (SELECT citta, count(*) as numero_arrivi
FROM arrpart ap, luogoaeroporto l
WHERE ap.arrivo = l.aeroporto
GROUP BY citta),

--media arrivi in ogni città
MediaArriviCitta as (SELECT avg(numero_arrivi) as media
FROM conteggioArriviPerCitta
)

SELECT citta
FROM MediaArriviCitta mac,conteggioArriviPerCitta mac1
WHERE mac.media <mac1.numero_arrivi;
-----------------------------------------------------

Domanda 4)

WITH durataMediaComp as (SELECT ap.comp, avg(durataminuti) as media_durata
FROM arrpart ap, luogoaeroporto l, Volo v
WHERE ap.partenza = l.aeroporto
AND l.nazione = 'Italy'
AND v.codice=ap.codice
GROUP BY ap.comp)
SELECT comp
FROM durataMediaComp
WHERE media_durata < (SELECT avg(media_durata) FROM durataMediaComp);
-----------------------------------------------------

Domanda 5)



WITH durataMediaPerCitta as (SELECT citta,avg(durataminuti) as durata_media
FROM arrpart ap join Volo v on v.codice=ap.codice, luogoaeroporto l
WHERE l.aeroporto = ap.arrivo
GROUP BY citta),

durataMediaVoli as (SELECT avg(durataminuti) as mediaTot
FROM arrpart ap join Volo v on v.codice=ap.codice, luogoaeroporto l
WHERE l.aeroporto = ap.arrivo),

	
devStandard as (SELECT stddev(durataminuti)
FROM arrpart ap join Volo v on v.codice=ap.codice, luogoaeroporto l
WHERE l.aeroporto = ap.arrivo)


SELECT citta,durata_media
FROM durataMediaVoli,durataMediaPerCitta,devStandard
WHERE ABS(durata_media-mediatot) > stddev;
-----------------------------------------------------

Domanda 6)

WITH mediaPartenzePerCitta as (SELECT l1.nazione,count(DISTINCT l1.citta) as num_citta
FROM arrpart ap, luogoaeroporto l1, luogoaeroporto l2
WHERE l1.aeroporto = ap.partenza
AND l2.aeroporto = ap.arrivo 
AND l1.nazione<>l2.nazione
GROUP BY l1.nazione)

SELECT * 
FROM mediaPartenzePerCitta mpc 
WHERE num_citta = (SELECT max(num_citta) FROM mediaPartenzePerCitta);
-----------------------------------------------------