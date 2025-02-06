#include "utils.hpp"
#ifndef CUSTOMER_CPP
#define CUSTOMER_CPP
class Customer
{
private:
public:
    int state = 0;
    vector<vector<double>> edge_probability;
    Customer(vector<vector<double>> *e)
    {
        edge_probability = *e;
    }
    Customer()
    {
        for (int i = 0; i < 2; i++)
        {
            vector<double> row(2, 0);
            edge_probability.push_back(row);
        }
    }
    int time_step()
    {
        double random_number = rand_float_0_1();
        double random_buf = 0;

        for (int i = 0; i < edge_probability[state].size(); i++)
        {

            random_buf += edge_probability[state][i];

            if ((random_number <= random_buf) || (random_buf >= 1))
            {
                state = i;
                break;
            }
        }

        return state;
    }

    void log()
    {
        cout << "\nMatrice probabilità :\n";
        for (auto &row : edge_probability)
        {
            for (auto &element : row)
            {
                cout << element << " ";
            }
            cout << "\n";
        }
    }
};

#endif