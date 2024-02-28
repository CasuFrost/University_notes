
<style>
    .edgeLabel {
        background: black !important;
        color: white !important;
    }
    .g.classGroup text	 {
        background: black !important;
        color: white !important;
    }
    body{
        background: white !important;
    }
    
</style>
```mermaid

%%{init:{
    'flowchart':{'nodeSpacing': 100, 'rankSpacing': 100},
    'themeVariables': {
      'lineColor': '#000'
    }
    }
    
}%%

classDiagram
    class Impiegato
    Impiegato : +String nome
    Impiegato : +String cognome
    Impiegato : +Timestamp data_nascita
    Impiegato : +float stipendio
    Impiegato : + Timestamp dep_data

    class Dipartimento
    Dipartimento : +String nome
    Dipartimento : +int numero
    
    class Associazione
    Associazione : +Timestamp inizio

    class Direzione
    Direzione : +Timestamp inizio

    class Progetto
    Progetto : +String nome
    Progetto : +float budget

    class Lavoro
    Lavoro : +Timestamp data_inizio
    
    
    Impiegato "1..1" --  "0..*" Associazione : afferisce
    Impiegato "1..1" --  "0..*" Direzione : dirige
    
    Direzione "0..*"  -- "1..1"Dipartimento: diretto
    Associazione "0..*"  -- "1..1"Dipartimento: associato
    Impiegato"1..1" --  "0..*" Lavoro : lavora
    Lavoro "0..*"  -- "1..1"Progetto : lavoro_progetto

     
    