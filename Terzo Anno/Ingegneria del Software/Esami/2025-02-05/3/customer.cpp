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
        /*calcolo nuovo stato*/
        double r = rand_float_0_1();
        if (state == 0)
        {
            if (r <= edge_probability[0][0])
            {
                state = 0;
                return 0;
            }
            else if (r <= edge_probability[0][1] + edge_probability[0][0])
            {
                state = 1;
                return 1;
            }
            else
            {
                state = 2;

                return 2;
            }
        }
        else if (state == 1)
        {
            if (r <= edge_probability[1][0])
            {
                state = 0;
                return 0;
            }
            else if (r <= edge_probability[1][1] + edge_probability[1][0])
            {
                state = 1;
                return 1;
            }
            else
            {
                state = 2;

                return 2;
            }
        }
        else if (state == 2)
        {
            if (r <= edge_probability[2][0])
            {
                state = 0;
                return 0;
            }
            else if (r <= edge_probability[2][1] + edge_probability[2][0])
            {
                state = 1;
                return 1;
            }
            else
            {
                state = 2;

                return 2;
            }
        }
        return 0;
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