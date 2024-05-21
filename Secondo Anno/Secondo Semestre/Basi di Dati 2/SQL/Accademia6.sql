Domanda 1 

SELECT posizione, count(*) 
FROM persona per 
GROUP BY posizione;
-----------------------------------------------------------------

Domanda 2 

SELECT count(*)
from persona 
where stipendio>=40000;
-----------------------------------------------------------------

Domanda 3

SELECT count(*)
FROM progetto  
WHERE budget>=50000 
and fine <= NOW();
-----------------------------------------------------------------

Domanda 4

SELECT avg(oredurata), max(oredurata), min(oredurata)
FROM progetto pr, attivitaprogetto  att
WHERE nome = 'Pegasus'
and att.progetto = pr.id;
-----------------------------------------------------------------

Domanda 5

SELECT per.id,per.nome,per.cognome,avg(oredurata), max(oredurata), min(oredurata)
FROM progetto pr, attivitaprogetto  att, persona per
WHERE pr.nome = 'Pegasus'
and att.progetto = pr.id
and per.id = att.persona	
GROUP BY per.nome,per.cognome,per.id;
-----------------------------------------------------------------

Domanda 6

SELECT per.id,per.nome,per.cognome, sum(att.oredurata)
FROM attivitanonprogettuale att, persona per
WHERE att.tipo='Didattica'
and att.persona = per.id
GROUP BY per.id,per.nome,per.cognome;
-----------------------------------------------------------------

Domanda 7

SELECT avg(stipendio),max(stipendio),min(stipendio)
FROM persona  
WHERE posizione='Ricercatore';
-----------------------------------------------------------------

Domanda 8

SELECT posizione,avg(stipendio),max(stipendio),min(stipendio)
FROM persona  
GROUP BY posizione;
-----------------------------------------------------------------

Domanda 9

SELECT pr.nome,sum(att.oredurata)
FROM persona per, attivitaprogetto att, progetto pr  
where att.persona = per.id 
and per.nome = 'Ginevra' 
and per.cognome = 'Riva'
and pr.id = att.progetto
GROUP BY pr.nome;
-----------------------------------------------------------------

Domanda 10

SELECT progetto
FROM (SELECT pr.nome as progetto, count(per.id) as lavoratori
FROM persona per, attivitaprogetto att, progetto pr  
where att.persona = per.id 
and pr.id = att.progetto
group by pr.nome)
where lavoratori>2;
-----------------------------------------------------------------

Domanda 11

SELECT per.id, nome, cognome 
FROM (
SELECT per.id,count(*)
FROM persona  per, progetto pr, attivitaprogetto att
WHERE per.posizione='Professore Associato'
and att.progetto=pr.id 
and att.persona=per.id
group by per.id) as q, persona per 
where per.id=q.id;
-----------------------------------------------------------------