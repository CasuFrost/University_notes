/*Questo file contiene solamente una classe per raggruppare comodamente
i dati relativi al costo di ogni team e del progetto totale*/

/*Ogni completamento di un progetto sarà correlato ad un istanza di questa classe*/
#include "utils.hpp"
using namespace std;

#ifndef DATA_HPP
#define DATA_HPP

class CostData
{
public:
    CostData() {}
    vector<int> cost_per_team;
    vector<int> days_per_team;
    int total_project_cost;
    int total_project_days;

    void print_information()
    {
        for (int k = 1; k <= W; k++)
        {
            cout << "team " << k << " giorni completamento : " << days_per_team[k] << ",    costo: " << cost_per_team[k] << " euro\n";
        }
        cout << "progetto totale ha impiegato " << total_project_days << " giorni ed un costo totale di " << total_project_cost << " euro\n";
    }
};

#endif