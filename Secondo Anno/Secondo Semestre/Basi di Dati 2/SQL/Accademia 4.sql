select distinct cognome from Persona;

select nome,cognome from Persona where 
posizione = 'Ricercatore';

select * from Persona where 
posizione = 'Professore Associato'
and cognome like 'V%'

select * from Persona where 
(posizione = 'Professore Associato' or 
posizione = 'Professore Ordinario'	)
and cognome like 'V%'

select * from Progetto where 
fine <= NOW();

select nome from Progetto order by inizio;

select nome from WP order by nome;

select distinct tipo from assenza;

select distinct tipo from attivitaprogetto;

select  distinct * from attivitanonprogettuale 
	where tipo = 'Didattica';