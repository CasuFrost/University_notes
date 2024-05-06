create domain PosInteger as Integer 
default 0 
check (value >= 0)

create domain NumeroOre as Integer 
default 0 
check (value >= 0 and value <= 8)

create domain Denaro  as Real 
default 0 
check (value >= 0)

create domain StringaM  as varchar(100) 

create type Strutturato  as enum ('Ricercatore', 'Professore Associato', 'Professore Ordinario')

create type LavoroProgetto as enum ('Ricerca e Sviluppo', 'Dimostrazione', 'Management', 'Altro')

create type LavoroNonProgettuale as enum ('Didattica', 'Ricerca', 'Missione', 'Incontro Dipartimentale', 'Incontro Accademico', 'Altro')

create type CausaAssenza as enum ('Chiusura Universitaria', 'Maternita', 'Malattia')

create table Persona (
	id PosInteger not null,
	nome  StringaM, 
	cognome  StringaM, 
	posizione  Strutturato,
	stipendio  Denaro,
	primary key (id)
)

create table Progetto(
	id PosInteger not null,
	nome  StringaM, 
	fine  date,
	inizio  date check(inizio<fine), 
	budget denaro,
	primary key (id),
	unique (nome)
)

create table WP (
	progetto PosInteger not null,
	id PosInteger not null,
	nome  StringaM not null, 
	fine  date,
	inizio  date check(inizio<fine), 
	primary key (id),
	unique nome,
	unique (progetto, id),
	foreign key (progetto) references Progetto(id)
)

create table AttivitaProgetto(
	id PosInteger not null,
	persona PosInteger not null,
	progetto PosInteger not null,
	wp PosInteger not null,
	giorno  date,
	tipo LavoroProgetto,
	oreDurata NumeroOre,
	primary key (id), 
	unique (wp),
	unique (progetto),
	foreign key (progetto, wp) references WP(progetto, id),
	foreign key (persona) references Persona(id)
)

create table AttivitaNonProgettuale(
	id PosInteger,
	persona PosInteger,
	tipo LavoroNonProgettuale, 
	giorno date,
	oreDurata NumeroOre,
	primary key (id), 
	foreign key (persona) references Persona(id)
)

create table Assenza(
	id PosInteger,
	persona PosInteger,
	tipo CausaAssenza,
	giorno date,
	primary key (id), 
	foreign key (persona) references Persona(id)
)