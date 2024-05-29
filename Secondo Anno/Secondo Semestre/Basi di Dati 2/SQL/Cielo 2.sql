Domanda 1)

SELECT a.codice, a.nome, count(distinct c.nome) as num_compagnie 
FROM Aeroporto a, Compagnia c, Volo v, Arrpart ap 
WHERE v.comp=c.nome
AND ap.codice=v.codice
AND ap.comp=c.nome
AND(ap.partenza=a.codice OR ap.arrivo=a.codice)
GROUP BY a.codice, a.nome
-----------------------------------------------------

Domanda 2)

SELECT count(*)
FROM Arrpart ap,volo v 
WHERE ap.partenza = 'HTR'
AND ap.codice=v.codice
AND durataminuti>=100;
-----------------------------------------------------

Domanda 3)

SELECT nazione,count(distinct a.codice)
FROM LuogoAeroporto l, Volo v, Aeroporto a, ArrPart ap
WHERE l.aeroporto = a.codice
AND v.codice=ap.codice
AND (ap.partenza = a.codice OR ap.arrivo = a.codice)
AND v.comp = 'Apitalia'
GROUP BY nazione;
-----------------------------------------------------

Domanda 4)

SELECT min(v.durataminuti) as minimo, max(v.durataminuti) as massimo, avg(v.durataminuti) as media
FROM Arrpart ap,volo v 
WHERE ap.comp='MagicFly'
AND ap.codice=v.codice;
-----------------------------------------------------

Domanda 5)

SELECT a.codice,a.nome,min(annofondaz)
FROM Compagnia c, ArrPart ap, Aeroporto a
WHERE c.nome = ap.comp
AND (a.codice = ap.arrivo or a.codice = ap.partenza)
GROUP BY a.codice, a.nome;
-----------------------------------------------------

Domanda 6)

SELECT l1.nazione, count( DISTINCT l2.nazione) as raggiungibili
FROM LuogoAeroporto l1, LuogoAeroporto l2,
	Aeroporto a1, Aeroporto a2, Volo v, ArrPart ap
WHERE l1.aeroporto = a1.codice
AND l2.aeroporto = a2.codice
AND l1.nazione<>l2.nazione
AND ap.codice = v.codice
AND ap.partenza = a1.codice
AND ap.arrivo = a2.codice
GROUP BY l1.nazione;
-----------------------------------------------------

Domanda 7)

SELECT partenza,avg(durataminuti) as durata_media
FROM Volo v, ArrPart ap
WHERE ap.codice = v.codice
GROUP BY partenza;
-----------------------------------------------------

Domanda 8)

SELECT c.nome, sum(durataminuti)
FROM Volo v join Compagnia c on  c.nome=v.comp
WHERE c.nome=v.comp
AND c.annofondaz>=1950
GROUP BY c.nome;
-----------------------------------------------------

Domanda 9)

SELECT codice, nome
FROM 	(SELECT  a.codice,a.nome, count(distinct comp) as compOp
		FROM ArrPart ap, Aeroporto a
		WHERE (ap.partenza = a.codice OR ap.arrivo= a.codice)
		GROUP BY a.codice,a.nome) 
WHERE compop=2;
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