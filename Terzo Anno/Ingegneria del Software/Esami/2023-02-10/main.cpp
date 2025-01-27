#include "dtmc.hpp"

double prob_not_move(int A, int B, int C, int D, int k, int i)
{
    return 1 - 1 / (double)(A + B * k * k + C * i * i + D * k * i);
    return (double)(1 - (double)(1 / (A + B * k * k + C * i * i + D * k * i)));
}
double alpha(int F, int G, int W, int k)
{
    return (double)(1 / (double)(F * (G * W - k)));
}

int main()
{
    srand((unsigned)time(NULL));
    setvbuf(stdout, NULL, _IONBF, 0);
    int A = 1, B = 1, C = 1, D = 1;
    int N = 5;
    int W = 3;
    int F = 1;
    int G = 2;
    vector<vector<double>> edge_prob;
    vector<DTMC> teams;

    for (int k = 0; k < W; k++)
    {
        /*creo la matrice di probabilità*/
        vector<vector<double>> edge_prob;
        vector<int> state;
        for (int i = 0; i < N; i++)
        {
            state.push_back(i);
            vector<double> raw;
            for (int j = 0; j < N; j++)
            {
                if (j != i)
                    raw.push_back(0);
                else
                    raw.push_back(prob_not_move(A, B, C, D, k + 1, i + 1));
            }
            edge_prob.push_back(raw);
        }
        edge_prob[N - 1][N - 1] = 1;
        DTMC tmp(state, edge_prob);
        teams.push_back(tmp);
    }

    for (int k = 0; k < W; k++)
    {
        /*Costi*/
        for (int i = 0; i < N; i++)
        {
            teams[k].state_cost[i] = (double)1000 - (double)500 * ((double)k / W - (double)1);
        }

        /*Probabilità*/
        teams[k].edge_prob[0][1] = 1 - teams[k].edge_prob[0][0];
        for (int i = 1; i < N - 1; i++)
        {
            teams[k].edge_prob[i][i + 1] = ((double)1 - alpha(F, G, W, k + 1)) * ((double)1 - teams[k].edge_prob[i][i]);
        }
        for (int i = 1; i < N - 2; i++)
        {
            for (int j = 0; j < i; j++)
            {
                teams[k].edge_prob[i][j] = alpha(F, G, W, k + 1) * ((1 - teams[k].edge_prob[i][i]) / (i));
            }
        }
    }

    /*riempimento della matrice di probabilità*/
    double expected_cost = 0;
    int steps_precision = 1000;
    vector<double> expected_time;
    for (int k = 0; k < W; k++)
    {
        double a = teams[k].expected_cost_mc_simulation(steps_precision, 2);
        expected_cost += a;
        double b = teams[k].expected_cost_mc_simulation(steps_precision, 3);
        expected_time.push_back(b);
        cout << "task team " << k + 1 << "\n       costo atteso : " << a
             << " EURO\n       tempo atteso : " << b << " giorni\n";
    }
    cout << "\ncosto atteso del progetto : " << expected_cost << " EURO\ntempo atteso del progetto : " << *max_element(expected_time.begin(), expected_time.end())
         << " giorni\n";

    ofstream MyFile("outputs.txt");
    time_t now = time(0);
    char buffer[80];
    tm *local_time = localtime(&now);
    strftime(buffer, sizeof(buffer), "%Y-%m-%d %H:%M:%S", local_time);
    MyFile << "Team AvgTime AvgCost StdDevTime StdDevCost(ID = " << 2046212 << ", MyMagicNumber = " << 1 + 2046212 % 173 << "," << " time = " << buffer << ")";
    // teams[0].printlog();
}