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

(SELECT DISTINCT id,nome,cognome FROM Persona) EXCEPT (
SELECT DISTINCT persona,NN,CC
FROM
	(SELECT DISTINCT per.id as persona, att.giorno as giornoLavoro, prog.nome as prog,per.nome as NN,per.cognome as CC
	FROM Persona per, attivitaprogetto att, Progetto prog 
	WHERE att.persona = per.id
	AND att.progetto = prog.id) q1 
WHERE prog<>'Pegasus' 
AND giornolavoro < (Select fine FROM Progetto WHere nome='Pegasus')
AND giornolavoro > (Select inizio FROM Progetto WHere nome='Pegasus')); 

 
--DA RIFARE, È SBAGLIATA
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