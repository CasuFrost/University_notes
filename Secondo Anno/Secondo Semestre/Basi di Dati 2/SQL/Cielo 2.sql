Domanda 1)

SELECT arrivo,count(comp)
FROM
	((SELECT DISTINCT comp, arrivo
	FROM arrpart ar)
	UNION
	(SELECT DISTINCT comp, partenza
	FROM arrpart ar))
GROUP BY arrivo;
-----------------------------------------------------

Domanda 2)

SELECT count(*)
FROM Arrpart ap,volo v 
WHERE ap.partenza = 'HTR'
AND ap.codice=v.codice
AND durataminuti>=100;
-----------------------------------------------------

Domanda 3)


-----------------------------------------------------

Domanda 4)

SELECT min(v.durataminuti) as minimo, max(v.durataminuti) as massimo, avg(v.durataminuti) as media
FROM Arrpart ap,volo v 
WHERE ap.comp='MagicFly'
AND ap.codice=v.codice;
-----------------------------------------------------

Domanda 5)


-----------------------------------------------------

Domanda 10)

SELECT citta 
FROM(SELECT citta, count(aeroporto) as apc
	FROM luogoaeroporto
	GROUP BY citta) 
WHERE apc>1;
-----------------------------------------------------

Domanda 11)

SELECT comp 
FROM (SELECT comp, avg(durataminuti) as dm 
	 FROM volo
	 GROUP BY comp)
WHERE dm>360;
-----------------------------------------------------

Domanda 12)

SELECT comp 
FROM (SELECT comp, min(durataminuti) as dm 
	 FROM volo
	 GROUP BY comp)
WHERE dm>100;
-----------------------------------------------------