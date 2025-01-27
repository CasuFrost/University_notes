
#include "utils.hpp"
using namespace std;

class DTMC
{
private:
    void read_from_file(string filename, int print = 0)
    {
        int num_state;
        ifstream file(filename);
        string line;
        getline(file, line);
        vector<string> words = splitString(line);
        if (words[0] == "N")
        {
            num_state = stoi(words[1]);
            if (print)
            {
                if (print)
                    cout << "numero stati : " << num_state << "\n";
            }
            for (int i = 0; i < num_state; i++)
            {
                state.push_back(i);
            }
            for (int i = 0; i < num_state; i++)
            {
                vector<double> tmp(state.size(), 0);
                edge_prob.push_back(tmp);
                edge_cost.push_back(tmp);
            }
        }
        else
        {
            printf("Parameter file ERROR\n");
            return;
        }
        while (getline(file, line))
        {
            words = splitString(line);
            int from = stoi(words[1]);
            int to = stoi(words[2]);
            double prob = stof(words[3]);
            double cost = stof(words[4]);
            if (print)
                cout << "   aggiungo arco da " << from << " a " << to << " con prob. " << prob << " e costo " << cost << "\n";
            edge_prob[from][to] = prob;
            edge_cost[from][to] = cost;
        }
        start_state = 0;
        end_state = state.size() - 1;
    }

    vector<int> state;
    int start_state;
    int current_state = 0;
    int end_state;
    vector<double> state_cost;
    vector<vector<double>> edge_prob; /*probabilità delle transizioni*/
    vector<vector<double>> edge_cost; /*probabilità delle transizioni*/

    void fix_cost()
    {
        if (state.size() == 0)
        {
            return;
        }
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
    DTMC(string filename)
    {
        read_from_file(filename);
        fix_cost();
    }
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

    double time_step(int cost_type)
    {
        double tmp_cost = 0;
        double random_number = ((double)rand() / (double)RAND_MAX);
        double random_buf = 0;

        for (int i = 0; i < edge_prob[current_state].size(); i++)
        {

            random_buf += edge_prob[current_state][i];

            if ((random_number <= random_buf) || (random_buf >= 1))
            {
                if (cost_type != 1)
                {
                    tmp_cost += edge_cost[current_state][i];
                }
                if (cost_type > 0)
                {
                    tmp_cost += state_cost[i];
                }
                current_state = i;

                break;
            }
        }
        return tmp_cost;
    }

    /*Esegue una simulazione del processo finché non termina, e ritorna il costo della simulazione*/
    double simulate_process(int cost_type)
    {
        current_state = 0;
        end_state = state.size() - 1;
        double tmp_cost = 0;
        while (current_state != end_state)
        {
            tmp_cost += time_step(cost_type);
        }
        current_state = 0;
        return tmp_cost;
    }

    /*Calcola il valore atteso dei costi in un'esecuzione del processo*/
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
        if (state.size() == 0)
        {
            printf("ERROR : zero states in the dtmc.\n");
            return 0;
        }

        vector<double> exptected_cost;
        for (int iter = 0; iter < steps; iter++)
        {
            double cost = simulate_process(cost_type);
            exptected_cost.push_back(cost);
        }

        /*Calcolo costo medio*/
        double avg = 0;
        for (int i = 0; i < exptected_cost.size(); i++)
        {
            avg += exptected_cost[i];
        }
        return avg / (double)steps;
    }

    /*Calcola la probabilità che il processo termini con un costo minore o uguale a max_cost*/
    double probability_max_cost(int steps, double max_cost, int cost_type)
    {
        double cost;
        int counter = 0;
        for (int i = 0; i < steps; i++)
        {
            cost = simulate_process(cost_type);
            if (cost <= max_cost)
                counter++;
        }
        return (double)counter / (double)steps;
    }

    /*Scrive in stoud le matrici di probabilità e dei costi*/
    void printlog()
    {
        cout << "stati: ";
        for (auto &element : state)
        {
            cout << element << " ";
        }
        cout << "\nMatrice probabilità :\n";
        for (auto &row : edge_prob)
        {
            for (auto &element : row)
            {
                cout << element << " ";
            }
            cout << "\n";
        }
        cout << "\nMatrice costi :\n";
        for (auto &row : edge_cost)
        {
            for (auto &element : row)
            {
                cout << element << " ";
            }
            cout << "\n";
        }
    }
};