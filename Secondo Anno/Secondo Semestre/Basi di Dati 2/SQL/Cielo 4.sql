Domanda 1)

WITH media AS (SELECT comp, avg(durataminuti) as media
FROM volo
GROUP BY comp)
SELECT * 
FROM volo v, media m WHERE 
m.comp=v.comp AND v.durataminuti > m.media;
-----------------------------------------------------

Domanda 2)

WITH citNumAr as (SELECT citta, count(*) as nap
FROM luogoaeroporto l
GROUP BY citta)
SELECT DISTINCT l.citta 
FROM aeroporto a, luogoaeroporto l,citNumAr cn, arrpart ap
WHERE a.codice=l.aeroporto
AND cn.citta=l.citta AND cn.nap>1
AND (ap.partenza = a.codice OR ap.arrivo=a.codice)
AND ap.comp = 'Apitalia';
-----------------------------------------------------

Domanda 3)

WITH coppie AS (SELECT ap.partenza as partenza ,a.codice as arrivo ,count(a.codice) as numvoli
FROM arrpart ap, aeroporto a
WHERE ap.arrivo = a.codice
GROUP BY ap.partenza,a.codice)
SELECT DISTINCT c1.partenza,c1.arrivo FROM coppie c1, coppie c2 
WHERE c1.partenza = c2.arrivo AND 
c1.arrivo = c2.partenza 
AND c1.numvoli=c2.numvoli;
-----------------------------------------------------

Domanda 4)

WITH media as (SELECT  comp, avg(durataminuti) as media
FROM volo
GROUP BY comp)
SELECT comp 
FROM media 
WHERE media.media > (SELECT avg(durataminuti) FROM volo);
-----------------------------------------------------

Domanda 5)


SELECT aeroporti 
FROM	(SELECT ap.partenza as aeroporti, count(distinct l1.nazione) as n
		FROM arrpart ap, luogoaeroporto l1
		WHERE l1.aeroporto=ap.arrivo
		GROUP BY ap.partenza )
WHERE n>1;
-----------------------------------------------------

Domanda 6)

WITH citNumAP as (SELECT l.citta as cit,count(l.aeroporto) as num
FROM luogoaeroporto l
GROUP BY l.citta)

SELECT DISTINCT v.codice,ap.partenza,ap.arrivo,ap.comp
FROM Volo v, arrpart ap, luogoaeroporto l,citNumAP
WHERE v.codice = ap.codice 
AND ap.partenza = l.aeroporto 
AND l.citta = citNumAP.cit 
AND num=1;
-----------------------------------------------------

Domanda 7)

WITH RECURSIVE tmp AS (
SELECT DISTINCT ap.arrivo as arr 
FROM arrpart ap 
WHERE ap.partenza = 'JFK'
	
	UNION

SELECT arrivo
FROM tmp, arrpart 
WHERE partenza = tmp.arr
AND partenza <> 'JFK'
)

SELECT * FROM tmp;
-----------------------------------------------------

Domanda 8)

WITH RECURSIVE par AS (SELECT DISTINCT lp2.citta as citDst
FROM arrpart ap, luogoaeroporto lp1,luogoaeroporto lp2
WHERE ap.partenza = lp1.aeroporto
AND lp2.aeroporto = ap.arrivo
AND lp1.citta = 'Roma'
	
	UNION ALL 
	
SELECT l2.citta
FROM arrpart ap,luogoaeroporto l, luogoaeroporto l2,par
WHERE ap.partenza = l.aeroporto
AND l.citta = par.citDst
AND l2.aeroporto = ap.arrivo
AND par.citDst <> 'Roma'
)
SELECT DISTINCT * FROM par;
-----------------------------------------------------

Domanda 9)

SELECT DISTINCT l.citta
FROM arrpart ap, arrpart ap2, luogoaeroporto l
WHERE ap.partenza = 'JFK'
AND ap2.partenza = ap.arrivo
AND ap2.arrivo = l.aeroporto;
-----------------------------------------------------