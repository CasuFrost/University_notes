Esercizio 1)

SELECT w.nome,w.inizio,w.fine
FROM Wp as w, Progetto as prj
WHERE w.progetto = prj.id AND prj.nome = 'Pegasus';

---------------------------------------------------------------------------------------------------------------------------------
Esercizio 2)

SELECT DISTINCT per.nome, per.cognome, per.posizione 
FROM AttivitaProgetto as att, Persona as per, Progetto as prj
WHERE att.persona = per.id and att.progetto = prj.id and prj.nome = 'Pegasus'
ORDER BY per.cognome DESC;

---------------------------------------------------------------------------------------------------------------------------------
Esercizio 3)

SELECT DISTINCT per.nome, per.cognome, per.posizione 
FROM AttivitaProgetto as att, AttivitaProgetto as att2, Persona as per, Progetto as prj
WHERE   att.persona = per.id 
	and att.progetto = prj.id 
	and prj.nome = 'Pegasus'
	and att2.persona = per.id 
	and att2.progetto = prj.id
	and att.id<>att2.id;

---------------------------------------------------------------------------------------------------------------------------------
Esercizio 4)

SELECT DISTINCT per.nome, per.cognome, per.posizione 
FROM Persona as per, Assenza as asz
WHERE per.posizione ='Professore Ordinario' 
	and asz.tipo = 'Malattia'
	and asz.persona = per.id;

---------------------------------------------------------------------------------------------------------------------------------
Esercizio 5)

SELECT DISTINCT per.nome, per.cognome, per.posizione 
FROM Persona as per, Assenza as asz, Assenza as asz2
WHERE per.posizione ='Professore Ordinario' 
	and asz.tipo = 'Malattia'
	and asz.persona = per.id
	and asz2.tipo = 'Malattia'
	and asz2.persona = per.id
	and asz2<>asz;

---------------------------------------------------------------------------------------------------------------------------------
Esercizio 6)

SELECT DISTINCT per.nome, per.cognome, per.posizione 
FROM Persona as per, attivitanonprogettuale as att
WHERE per.posizione ='Ricercatore' 
and 	per.id = att.persona
and 	att.tipo = 'Didattica';

---------------------------------------------------------------------------------------------------------------------------------
Esercizio 7)

SELECT DISTINCT per.nome, per.cognome, per.posizione 
FROM Persona as per, attivitanonprogettuale as att, attivitanonprogettuale as att2
WHERE per.posizione ='Ricercatore' 
and 	per.id = att.persona
and 	att.tipo = 'Didattica'
and 	per.id = att2.persona
and 	att2.tipo = 'Didattica'
and 	att2<>att;

---------------------------------------------------------------------------------------------------------------------------------
Esercizio 8) 

SELECT DISTINCT per.nome, per.cognome
FROM attivitaprogetto as attprj, attivitanonprogettuale as attnprj, persona as per
WHERE per.id = attprj.persona 
and   per.id = attnprj.persona 
and   attprj.giorno = attnprj.giorno;
 
---------------------------------------------------------------------------------------------------------------------------------
Esercizio 9) 

SELECT DISTINCT per.nome, per.cognome, attprj.giorno, attnprj.tipo as tipoAttivitàNonProgettuale,
prj.nome as nomeProgetto, attprj.oredurata as oreAttivitàProgettuale, attnprj.oredurata as oreAttivitàNonProgettuale
FROM attivitaprogetto as attprj, attivitanonprogettuale as attnprj, persona as per, progetto as prj
WHERE per.id = attprj.persona 
and   per.id = attnprj.persona 
and   attprj.giorno = attnprj.giorno
and   prj.id = attprj.progetto;

---------------------------------------------------------------------------------------------------------------------------------
Esercizio 10) 

SELECT DISTINCT per.nome, per.cognome
FROM persona as per, assenza as asz, attivitaprogetto as att
WHERE att.persona = per.id
and asz.persona = per.id
and asz.giorno = att.giorno;

---------------------------------------------------------------------------------------------------------------------------------
Esercizio 11) 

SELECT DISTINCT per.nome, per.cognome, asz.giorno, prj.nome as nomeProgetto, att.oredurata as oreAttivitàProgettuale
FROM persona as per, assenza as asz, attivitaprogetto as att, progetto as prj
WHERE att.persona = per.id
and asz.persona = per.id
and asz.giorno = att.giorno
and prj.id = att.progetto;

---------------------------------------------------------------------------------------------------------------------------------
Esercizio 12) 

SELECT DISTINCT w1.nome
FROM  wp as w1, wp as w2, progetto as prj, progetto as prj2
WHERE w1.nome=w2.nome 
and w1.progetto = prj.id
and w2.progetto = prj2.id
and prj <> prj2;