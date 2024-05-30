Domanda 1)

SELECT posizione, avg(stipendio) as media, 
	stddev(stipendio) as deviazione_standard
FROM Persona
GROUP BY posizione;
--------------------------------------------------

Domanda 2)

SELECT distinct *
FROM Persona per
WHERE per.stipendio > (SELECT avg(stipendio)
	FROM Persona
	WHERE posizione = per.posizione);
--------------------------------------------------

Domanda 3)

SELECT per2.posizione,count(per2.id) 
	FROM Persona per2, (SELECT posizione, avg(stipendio) as media, 
	stddev(stipendio) as deviazione_standard
	FROM Persona
	GROUP BY posizione) Q
WHERE Q.posizione=per2.posizione
AND ABS(per2.stipendio-media)<=deviazione_standard
GROUP BY per2.posizione;
--------------------------------------------------

Domanda 4)

SELECT * FROM (SELECT per.id, per.nome, per.cognome, sum(oredurata) as ore
			FROM Persona per join Attivitaprogetto att on att.persona=per.id
			GROUP BY per.id, per.nome, per.cognome)
WHERE ore>=20;
--------------------------------------------------

Domanda 5)

SELECT nome,(fine-inizio) as durata
FROM Progetto WHERE (fine-inizio)>(
SELECT avg(fine-inizio) as durata
FROM Progetto pr);
--------------------------------------------------

Domanda 6)

SELECT nome,sum(oredurata) as durata_complessiva
FROM Progetto pr  join attivitaprogetto att on att.progetto=pr.id
WHERE fine<NOW()
AND tipo = 'Dimostrazione'
GROUP BY nome;
--------------------------------------------------

Domanda 7)

SELECT * FROM 
	(SELECT per.id, per.nome, per.cognome, count(distinct ass.id) as assenze
	FROM Persona per join assenza ass on ass.persona=per.id
	WHERE posizione='Professore Ordinario'
	AND ass.tipo='Malattia'
	GROUP BY per.id, per.nome, per.cognome)
WHERE assenze > (
	SELECT avg(assenze2) FROM 
	(SELECT per.id, per.nome, per.cognome, count(distinct ass.id) as assenze2
	FROM Persona per join assenza ass on ass.persona=per.id
	WHERE posizione='Professore Associato'
	AND ass.tipo='Malattia'
	GROUP BY per.id, per.nome, per.cognome)
)
--------------------------------------------------