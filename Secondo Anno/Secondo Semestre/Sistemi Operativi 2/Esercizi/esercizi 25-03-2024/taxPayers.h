#define MAX_TP 10

typedef struct
{
	int year;
	int month;
	int day;
} birthdate_t;

typedef struct
{
	char ID[17]; // ad es: codice fiscale
	long int income;
	float taxRate;
	birthdate_t bd;
} taxpayer_t; // nome del nuovo tipo di dato

taxpayer_t *newTP(char *id, long int inc, float rate, birthdate_t b)
{

	taxpayer_t *pTP = malloc(sizeof(taxpayer_t));
	strcpy(pTP->ID, id); // using ->
	// strcpy( pTP.ID, id );	 // Da errore
	pTP->income = inc; // using ->
	(*pTP).taxRate = rate;

	pTP->bd = b;

	return pTP;
}

taxpayer_t *newTPValue(char *id, long int inc, float rate, birthdate_t bd)
{

	taxpayer_t *pTP = malloc(sizeof(taxpayer_t));
	strcpy(pTP->ID, id); // using ->
	pTP->income = inc;	 // using ->
	//(*pTP).taxRate = rate;
	pTP->taxRate = rate;
	(*pTP).bd.year = bd.year;
	(*pTP).bd.month = bd.month;
	(*pTP).bd.day = bd.day;

	return pTP;
}

taxpayer_t *newTPRif(char *id, long int inc, float rate, birthdate_t *bd)
{

	taxpayer_t *pTP = malloc(sizeof(taxpayer_t));
	strcpy(pTP->ID, id); // using ->
	pTP->income = inc;	 // using ->
	(*pTP).taxRate = rate;
	//(*pTP).bd.year=(*bd).year;
	pTP->bd.year = bd->year;
	(*pTP).bd.month = (*bd).month;
	(*pTP).bd.day = (*bd).day;

	return pTP;
}
