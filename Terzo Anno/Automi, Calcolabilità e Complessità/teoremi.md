# automi  
Chiusura di REG (unione intersezione complemento) 

DFA è equivalente NFA 

Chiusura di REG (concatenazione e star) 

Equivalenza DFA ed Espressioni regolari 

Pumping Lemma per espressioni regolari 

forma normale CFG 

equivalenza PDA e CFG

Pumping Lemma per CFG

# calcolabilità

TM multinastro è equivalente ad una TM

NTM è equivalente ad una TM

$A_{TM}$ è turing riconoscibile

$\mathbb R$ non è numerabile

esistono linguaggi non riconoscibili (TM sono numerabili, i linguaggi no)

$A_{TM}$ non è turing decidibile (diagonalizzazione)

$HALT_{TM}$ non è turing decidibile

$E_{TM}$ non è decidibile.

Se $A\le_m B$ e $B$ è decidibile, allora  anche $A$ è decidibile.

Teoremi di incompletezza $\mathcal I$ e $\mathcal {II}$

# complessità di tempo

$2-SAT$ è in $P$

$3-COL$ è in $NP$

$P\subseteq NP \subseteq EXP$

Le due definizioni di $NP$ sono equivalenti

Se $SAT$ è in $P$, anche $4-COL$ è in P

Dimostrazioni varie sulla riduzione

Teorema di Cook-Levin

 Se $S$ è un linguaggio $NP$ completo, allora $S\in P \iff P=NP$

 $P=NP\implies EXP=NEXP$

$SAT\in P \iff UNSAT \in P$

 $P=coP$

 $coNP\subseteq EXP$

 $P\subseteq coNP$

 $UNSAT$ è $coNP$ completo

  # complessità di spazio

  $DTIME(f(n))\subseteq SPACE(f(n))$

  Per ogni $f(n)\ge \log(n)$ si ha che $SPACE(f(n))\subseteq DTIME(2^{O(f(n))})$

  $PATH \in SPACE(\log^2(n))$
  
  $PATH \in NLOG$

  $NLOG \subseteq P$ e   $NLOG \subseteq SPACE(\log^2(n))$

  $PATH$ è $NLOG$ completo

Se $P$ e $Q$ sono computabili in spazio $O(\log(n))$, allora lo è anche $R = P \circ Q$

 $TQBF$ è in $PSPACE$

  $TQBF$ è $PSPACE$ difficile

  Teorema (Immerman-Szelepcsényi)

  Teorema di Gerarchia di Tempo