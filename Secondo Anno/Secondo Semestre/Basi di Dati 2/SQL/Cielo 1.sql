Domanda 1)

Select  codice, comp as compagnia
from volo v
where v.durataminuti>180;
-----------------------------------------------------

Domanda 2)

Select distinct comp.nome
from volo v, compagnia comp 
where v.durataminuti>180 and 
v.comp = comp.nome;
-----------------------------------------------------

Domanda 3)

SELECT volo.codice, volo.comp
FROM volo, arrpart, aeroporto 
WHERE arrpart.codice = volo.codice
AND arrpart.partenza = aeroporto.codice
AND aeroporto.codice = 'CIA';
-----------------------------------------------------

Domanda 4)

SELECT DISTINCT volo.comp
FROM volo, arrpart, aeroporto 
WHERE arrpart.codice = volo.codice
AND arrpart.arrivo = aeroporto.codice
AND aeroporto.codice = 'FCO';
-----------------------------------------------------

Domanda 5)

SELECT volo.codice, volo.comp
FROM volo, arrpart
WHERE arrpart.codice = volo.codice
AND arrpart.partenza = 'FCO'
AND arrpart.arrivo = 'JFK';
-----------------------------------------------------

Domanda 6)

SELECT DISTINCT volo.comp
FROM volo, arrpart
WHERE arrpart.codice = volo.codice
AND arrpart.partenza = 'FCO'
AND arrpart.arrivo = 'JFK';
-----------------------------------------------------

Domanda 7)

SELECT DISTINCT volo.comp
FROM volo, aeroporto aa, luogoaeroporto la, arrpart,aeroporto ap, luogoaeroporto lp
WHERE volo.codice=arrpart.codice
AND arrpart.arrivo=aa.codice
AND arrpart.partenza=ap.codice
AND aa.codice = la.aeroporto
AND ap.codice = lp.aeroporto
AND la.citta = 'New York'
AND lp.citta = 'Roma';
-----------------------------------------------------

Domanda 8)

SELECT DISTINCT aeroporto.codice, aeroporto.nome, luogoaeroporto.citta, luogoaeroporto.nazione
FROM volo v, arrpart ,aeroporto, luogoaeroporto
WHERE v.comp = 'MagicFly'
AND arrpart.codice = v.codice
AND arrpart.arrivo = aeroporto.codice
AND aeroporto.codice = luogoaeroporto.aeroporto;
-----------------------------------------------------

Domanda 9)

SELECT  DISTINCT v.codice, v.comp, ap.codice, aa.codice
FROM volo v, arrpart ,aeroporto ap, luogoaeroporto lp, aeroporto aa, luogoaeroporto la
WHERE ap.codice = lp.aeroporto 
AND aa.codice = la.aeroporto
AND arrpart.codice = v.codice
AND arrpart.arrivo = aa.codice 
AND arrpart.partenza = ap.codice
AND la.citta = 'New York'
And lp.citta = 'Roma';
-----------------------------------------------------

Domanda 10)

-----------------------------------------------------

Domanda 11)

SELECT DISTINCT volo.comp
FROM volo, arrpart, compagnia
WHERE arrpart.codice = volo.codice
AND arrpart.partenza = 'FCO'
AND arrpart.arrivo = 'JFK'
AND volo.comp = compagnia.nome
AND compagnia.annofondaz IS NOT NULL;
-----------------------------------------------------