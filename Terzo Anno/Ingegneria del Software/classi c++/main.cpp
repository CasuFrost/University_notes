#include "dtmc.hpp"
using namespace std;
int main()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    vector<int> state = {0, 1, 2, 3};
    vector<vector<double>> edge_prob;
    vector<vector<double>> edge_cost;

    for (int i = 0; i < state.size(); i++)
    {
        vector<double> tmp(state.size(), 0);
        edge_prob.push_back(tmp);
        vector<double> tmp2(state.size(), 0);
        edge_cost.push_back(tmp2);
    }
    edge_prob[0][1] = 1;
    edge_prob[1][2] = 0.7;
    edge_prob[1][3] = 0.3;
    edge_prob[3][3] = 1;
    edge_prob[2][3] = 1;

    edge_cost[0][1] = 100;
    edge_cost[1][2] = 100;
    edge_cost[1][3] = 150;
    edge_cost[3][3] = 0;
    edge_cost[2][3] = 100;

    DTMC m_chain(state, edge_prob, edge_cost);
    cout << "expected cost : " << m_chain.expected_cost_mc_simulation(1000, 2) << "\n";
}