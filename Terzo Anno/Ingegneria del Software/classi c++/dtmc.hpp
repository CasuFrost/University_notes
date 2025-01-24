#include <iostream>
#include <vector>
#include <random>
#include <time.h>
#include <cstring>
#include <string>
#include <sstream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

class DTMC
{
private:
    vector<int> state;
    int start_state;
    int end_state;
    vector<double> state_cost;
    vector<vector<double>> edge_prob; /*probabilità delle transizioni*/
    vector<vector<double>> edge_cost; /*probabilità delle transizioni*/

    void fix_cost()
    {
        if (edge_cost.size() == 0)
        {
            for (int i = 0; i < state.size(); i++)
            {
                vector<double> tmp(state.size(), 0);
                edge_cost.push_back(tmp);
            }
        }
        if (state_cost.size() == 0)
        {
            for (int i = 0; i < state.size(); i++)
            {
                state_cost.push_back(0);
            }
        }
    }

public:
    DTMC(vector<int> state, vector<double> state_cost, vector<vector<double>> edge_prob, vector<vector<double>> edge_cost)
    {
        this->state = state;
        this->state_cost = state_cost;
        this->edge_prob = edge_prob;
        this->edge_cost = edge_cost;
        start_state = 0;
        end_state = state.size() - 1;
    }
    DTMC(vector<int> state, vector<vector<double>> edge_prob, vector<double> state_cost)
    {
        this->state = state;
        this->edge_prob = edge_prob;
        this->state_cost = state_cost;
        start_state = 0;
        end_state = state.size() - 1;
        fix_cost();
    }
    DTMC(vector<int> state, vector<vector<double>> edge_prob, vector<vector<double>> edge_cost)
    {
        this->state = state;
        this->edge_prob = edge_prob;
        this->edge_cost = edge_cost;
        start_state = 0;
        end_state = state.size() - 1;
        fix_cost();
    }
    DTMC(vector<int> state, vector<vector<double>> edge_prob)
    {
        this->state = state;
        this->edge_prob = edge_prob;
        start_state = 0;
        end_state = state.size() - 1;
        fix_cost();
    }

    double expected_cost_mc_simulation(int steps, int cost_type)
    {
        /*Error detection*/

        /* cost_type = 1 calcola il costo degli archi
           cost_type = 0 calcola il costo degli stati
           cost_type = 2 di entrambi*/
        if (cost_type < 0 || cost_type > 2)
        {
            printf("invalid argoument : cost_type should be 0, 1 or 2\n");
            return -1;
        }

        srand((unsigned)time(NULL));
        if (state.size() == 0)
        {
            printf("ERROR : zero states in the dtmc.\n");
            return 0;
        }
        vector<double> exptected_cost;
        for (int iter = 0; iter < steps; iter++)
        {
            int curr_state = start_state;

            double tmp_cost = 0;
            while (curr_state != end_state)
            {
                double random_number = ((double)rand() / (double)RAND_MAX);
                double random_buf = 0;

                for (int i = 0; i < edge_prob[curr_state].size(); i++)
                {
                    random_buf += edge_prob[curr_state][i];

                    if ((random_number <= random_buf) || (random_buf >= 1))
                    {
                        if (cost_type != 1)
                        {
                            tmp_cost += edge_cost[curr_state][i];
                        }
                        if (cost_type > 0)
                        {
                            tmp_cost += state_cost[i];
                        }
                        curr_state = i;

                        break;
                    }
                }
            }

            exptected_cost.push_back(tmp_cost);
        }

        /*Calcolo costo medio*/
        double avg = 0;
        for (int i = 0; i < exptected_cost.size(); i++)
        {
            avg += exptected_cost[i];
        }

        return avg / (double)steps;
    }
};