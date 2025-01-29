#include "utils.hpp"
#include "dtmc.hpp"
#include "data.hpp"
#include "env.hpp"
#include "monitor.hpp"
#include "dispatcher.hpp"
#include "hoven.hpp"
#include "server.hpp"
#include "controller.hpp"
#include <unistd.h>

double tau(int i, int k) { return (double)A + (double)B * (double)k * (double)k + (double)C * (double)i * (double)i + (double)D * (double)k * (double)i; }
double prob_same_spot(int i, int k)
{
    return (double)1 - (1 / (tau(i, k)));
}

double alpha(int k)
{
    double den = (double)F * ((double)G * (double)W - (double)k);
    return (double)1 / den;
}

int team_cost(int k)
{
    return (int)(1000 - 500 * ((double)(k - 1) / (double)(W - 1)));
}

CostData simulate_project(vector<DTMC> teams, int debug = 0)
{
    CostData data;
    for (int k = 1; k <= W; k++) /*Per ogni team re-imposto lo stato iniziale ad 1*/
    {
        teams[k].start_state = 1;
        teams[k].current_state = 1;
    }
    int team_in_final_state = 0;
    int time = 1;
    vector<int> cost_per_team(W + 2);
    vector<int> days_per_team(W + 2);
    int total_cost = 0;
    while (team_in_final_state < W) /*eseguo finché tutti i team sono arrivati allo stato N*/
    {
        for (int k = 1; k <= W; k++) /*Per ogni team*/
        {
            if (teams[k].current_state != N)
            {
                int cost = teams[k].time_step(1);
                cost_per_team[k] += cost;
                total_cost += cost;
                if (teams[k].current_state == N)
                {
                    cost_per_team[k] += cost;
                    total_cost += cost;
                    /*Passando allo stato N il costo diventa zero, si calcola però un giorno di costo in più, ossia il costo di permanere nello stato
                     N per una sola volta*/

                    team_in_final_state++;
                    days_per_team[k] = time;
                    if (debug)
                        cout << "team " << k << " termina la sua task in " << time << " giorni con un costo di " << cost_per_team[k] << " euro\n";
                }
            }
        }
        time++;
    }
    data.cost_per_team = cost_per_team;
    data.days_per_team = days_per_team;
    data.total_project_cost = total_cost;
    data.total_project_days = max_buffer(days_per_team);
    if (debug)
        cout << "il progetto ha richiesto in totale " << max_buffer(days_per_team) << " giorni e " << total_cost << " euro\n";
    return data;
}

void ex1(int steps)
{
    vector<DTMC> teams(W + 2); /*considero i team da teams[1] a teams[W]*/

    for (int k = 1; k <= W; k++) /*Per ogni team*/
    {
        /*Costruisco una matrice di probabilità N+2 x N+2 ma considero solo gli elementi da 1 ad N, escludendo gli elementi 0 e N+1*/
        vector<vector<double>> edge_prob(N + 1);
        for (int i = 0; i < N + 1; i++)
        {
            vector<double> row(N + 1);
            edge_prob[i] = row;
        }

        /*come prima cosa riempio la diagonale con le prob. p_{i,i}(k) escludendo p_{N,N}(k) che è sempre 1*/
        for (int i = 1; i <= N - 1; i++)
        {
            edge_prob[i][i] = prob_same_spot(i, k);
        }
        edge_prob[N][N] = 1; /*quando un team giunge nello stato N ci resta, finché tutti i team non sono nello stato N*/
        edge_prob[1][2] = (double)1 - edge_prob[1][1];

        /*probabilità di passare al successivo*/
        for (int i = 2; i <= N - 1; i++)
        {
            edge_prob[i][i + 1] = ((double)1 - alpha(k)) * ((double)1 - edge_prob[i][i]);
        }

        /*probabilità di retrocedere*/
        for (int i = 2; i <= N - 1; i++)
        {
            for (int j = 1; j <= i - 1; j++)
            {
                edge_prob[i][j] = alpha(k) * ((double)1 - edge_prob[i][i]) / ((double)i - (double)1);
            }
        }

        /*print della matrice di probabilità*/
        if (DEBUG)
        {
            cout << "\nteam " << k << " :\n";
            for (int i = 1; i <= N; i++)
            {
                for (int j = 1; j <= N; j++)
                {
                    cout << edge_prob[i][j] << " | ";
                }
                cout << "\n";
            }
        }

        vector<int> states;
        vector<double> state_cost;
        for (int i = 0; i <= N; i++)
        {
            states.push_back(i);
            state_cost.push_back(team_cost(k));
        }
        state_cost[N] = 0; /*nella fase finale, il team non ha costo*/
        DTMC team(states, edge_prob, state_cost);
        team.start_state = 1;
        team.current_state = 1;
        teams[k] = team;
    }

    /*i seguenti vettori sono relativi al calcolo della media e rappresentano più simulazioni di un progetto*/
    vector<vector<int>> team_days_vector(W + 2); /*per ogni team si hanno i tempi di completamento della task*/
    vector<vector<int>> team_cost_vector(W + 2); /*per ogni team si hanno i costi di completamento della task*/
    vector<int> total_cost_vector;               /*vettori con i costi totali*/
    vector<int> total_days_vector;               /*tempi totali*/

    /*Simulazione di un progetto*/
    vector<CostData> project_simulations;
    for (int i = 0; i < steps; i++)
    {
        CostData simulation = simulate_project(teams);
        for (int k = 1; k <= W; k++) /*per ogni team*/
        {
            team_days_vector[k].push_back(simulation.days_per_team[k]);
            team_cost_vector[k].push_back(simulation.cost_per_team[k]);
        }
        total_cost_vector.push_back(simulation.total_project_cost);
        total_days_vector.push_back(simulation.total_project_days);
        /*A questo punto ha terminato un progetto*/
    }
    if (DEBUG)
        cout << "con " << steps << " progetti : \n";
    for (int k = 1; k <= W; k++) /*per ogni team*/
    {
        if (DEBUG)
        {
            cout << "  -per il team " << k << " :\n";
            cout << "        * tempo medio fine di un task " << (int)avg_buffer(team_days_vector[k]) << "\n";
            cout << "        * costo medio fine di un task " << (int)avg_buffer(team_cost_vector[k]) << "\n";
        }
    }
    if (DEBUG)
    {
        cout << "  -tempo medio fine progetto " << (int)avg_buffer(total_days_vector) << "\n";
        cout << "  -costo medio  progetto " << (int)avg_buffer(total_cost_vector) << "\n";
        cout << "--------------------------------------------\n\n";
    }
    ofstream file("output/outputs1.txt");
    file << "ID = 2046212, MyMagicNumber = " << 1 + 2046212 % 173 << ", time = " << getCurrentTimeString()
         << "\n";
    file << "A=" << A << ", ";
    file << "B=" << B << ", ";
    file << "C=" << C << ", ";
    file << "D=" << D << ", ";
    file << "F=" << F << ", ";
    file << "G=" << G << ", ";
    file << "N=" << N << ", ";
    file << "W=" << W << ", ";
    file << "AvgTime=" << (int)avg_buffer(total_days_vector) << ", ";
    file << "AvgCosto=" << (int)avg_buffer(total_cost_vector) << "\n";
    for (int k = 1; k <= W; k++) /*per ogni team*/
    {
        file << k << " " << (int)avg_buffer(team_days_vector[k]) << " " << avg_buffer(total_cost_vector) << " ";
        file << (int)stdev_buffer(team_days_vector[k]) << " " << stdev_buffer(total_cost_vector) << "\n";
    }
    file.close();
}

void ex2()
{
    Env env;
    Monitor monitor;

    for (int i = 0; i < HORIZON; i++)
    {
        monitor.time_step(i, env.time_step());
    }
    ofstream file("output/outputs2.txt");
    file << "ID = 2046212, MyMagicNumber = " << 1 + 2046212 % 173 << ", time = " << getCurrentTimeString()
         << "\n";
    file << monitor.avg_time_gap() << " " << monitor.stddev_time_gap();
    file.close();
}

void ex3(int ex4 = 0)
{
    Dispatcher dispatcher;
    Env env;
    vector<Server> servers;
    for (int i = 0; i < Q; i++)
    {
        Server s;
        servers.push_back(s);
    }

    for (int time = 0; time < HORIZON; time++)
    {
        dispatcher.time_step(env.time_step(), time, &servers);

        /*server work*/
        for (int i = 0; i < Q; i++)
        {
            servers[i].time_step(time);
        }
    }
    ofstream file;
    if (!ex4)
    {
        file.open("output/outputs3.txt");
        file << "ServerID AvgResp StdDevResp (ID=2046212, MyMagicNumber=" << 1 + 2046212 % 173 << ", HORIZON=" << HORIZON << ", time = " << getCurrentTimeString()
             << ")\n";
        for (int i = 0; i < Q; i++)
        {
            if (servers[i].time_to_response.size() != 0)
                file << i << " " << (int)avg_buffer(servers[i].time_to_response) << " " << (int)stdev_buffer(servers[i].time_to_response) << "\n";
        }
    }
    else
    {
        ofstream file("output/outputs4.txt");
        file << "OutputIndex Load (ID=2046212, MyMagicNumber=" << 1 + 2046212 % 173 << ", HORIZON=" << HORIZON << ", time = " << getCurrentTimeString()
             << ")\n";
        for (int i = 0; i < Q; i++)
        {
            file << i << " " << servers[i].load_balance() << "\n";
        }
    }
    file.close();
}

void ex5()
{
    Oven oven;
    Controller controller;
    int iteration = 0;
    double second_passed;
    double x = 0;
    double x1 = 0;
    double r = 100;
    double u = 0;
    vector<double> errors;
    for (int i = 0; i < 10000 * HORIZON; i++) /*un'iterazione rappresenta T secondi*/
    {
        // system("clear");
        //  cout << "segnale di controllo :" << u;
        //  cout << "\nerrore :" << x - r;
        errors.push_back(x - r);
        // cout << "\nstato del forno :" << x << "\n\n";
        second_passed += T;
        u = controller.time_step(x, x1, r);
        oven.time_step(u, T);
        x = oven.x;
        x1 = oven.x1;
        iteration++;
    }
    ofstream file("output/outputs5.txt");
    file << "AvgErr StdDevErr (ID=2046212, MyMagicNumber=" << 1 + 2046212 % 173 << ", HORIZON=" << HORIZON << ", time = " << getCurrentTimeString()
         << ")\n";
    file << (int)avg_buffer(errors) << " " << (int)stdev_buffer(errors);

    file.close();
}
void ex4()
{
    ex3(1);
}

int main(int argc, char **argv)
{
    setvbuf(stdout, NULL, _IONBF, 0);
    srand((unsigned)time(NULL));
    ex1(HORIZON);
    ex2();
    ex3();
    ex4();
    ex5();
}