Domanda 1)

--------------------------------------------------

Domanda 2)
SELECT distinct *
FROM Persona per
WHERE per.stipendio > (SELECT avg(stipendio)
	FROM Persona
	WHERE posizione = per.posizione);
--------------------------------------------------

Domanda 3)

--------------------------------------------------

Domanda 4)

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

--------------------------------------------------