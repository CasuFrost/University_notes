Domanda 1)

(SELECT id, nome, cognome
FROM PERSONA) 
	EXCEPT
(SELECT per.id, per.nome, per.cognome
FROM Persona per, Assenza ass, attivitaprogetto att, attivitanonprogettuale attnp 
WHERE per.id = ass.persona
AND per.id = att.persona
AND per.id = attnp.persona
AND (ass.giorno = att.giorno OR ass.giorno = attnp.giorno)); 
--------------------------------------------------

Domanda 2)

WITH inizio_fine_Pegasus as (SELECT inizio as inizio_pegasus, fine as fine_pegasus
FROM Progetto prog
WHERE prog.nome='Pegasus'),


persone_partecipanti_durante_pegasus as (SELECT DISTINCT att.persona
FROM  Attivitaprogetto att, inizio_fine_Pegasus ifp
WHERE att.giorno >=ifp.inizio_pegasus
AND att.giorno <= ifp.fine_pegasus)


	
SELECT personeBuone.id,nome,cognome FROM	
	(SELECT id FROM Persona EXCEPT
SELECT * FROM persone_partecipanti_durante_pegasus) as personeBuone join Persona per on per.id=personeBuone.id
ORDER BY personeBuone.id ASC;
--------------------------------------------------

Domanda 3)

SELECT id, nome,cognome, stipendio
FROM Persona per 
WHERE posizione = 'Ricercatore' AND 
stipendio>=(
	SELECT max(stipendio)
	FROM Persona 
	WHERE posizione = 'Professore Associato' OR 
	posizione = 'Professore Ordinario'
);
--------------------------------------------------

Domanda 4)

SELECT per.id,per.nome,per.cognome
FROM Progetto pr, AttivitaProgetto att, Persona per
WHERE pr.budget > (SELECT avg(budget) FROM Progetto)
AND att.progetto  = pr.id
AND att.persona = per.id;
--------------------------------------------------

Domanda 5)

WITH Q AS (SELECT att.progetto, sum(oredurata) as somma 
	FROM AttivitaProgetto att
	WHERE tipo = 'Ricerca e Sviluppo'
	GROUP BY att.progetto)

SELECT pr.nome 
FROM Q, Progetto pr
WHERE 
somma > (SELECT avg(somma) FROM
	Q)
AND pr.id = progetto
AND pr.budget < (SELECT avg(budget) FROM Progetto);
--------------------------------------------------