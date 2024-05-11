select wp.inizio,wp.fine from wp,progetto  where 
progetto.id = wp.progetto and progetto.nome = 'Pegasus'

select distinct Persona.nome,Persona.cognome,Persona.posizione from Persona,attivitaprogetto,progetto where 
persona.id = attivitaprogetto.persona and 
attivitaprogetto.progetto = progetto.id and 
progetto.nome = 'Pegasus'
	order by Persona.cognome desc;

QUERY 3

select distinct Persona.nome,Persona.cognome,Persona.posizione from Persona,assenza where 
persona.id = assenza.persona and 
	persona.posizione = 'Professore Ordinario' and 
	tipo = 'Malattia';