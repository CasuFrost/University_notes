#include "customer.hpp"

class Monitor
{
private:
    int registred_request = 0;
    int time_without_req = 0;
    vector<int> registred_time_gap;

public:
    Monitor()
    {
    }
    void simulate_step(int request)
    {
        if (request)
        {
            registred_request++;
            registred_time_gap.push_back(time_without_req);
            time_without_req = 0;
        }
        else
        {
            time_without_req++;
        }
    }

    int avg_esteem()
    {
        return (int)accumulate(registred_time_gap.begin(), registred_time_gap.end(), 0.0) / registred_time_gap.size();
    }

    int var_esteem()
    {
        double varianza = 0.0;
        for (int numero : registred_time_gap)
        {
            varianza += pow(numero - avg_esteem(), 2);
        }
        varianza /= registred_time_gap.size();
        return (int)varianza;
    }

    int stdev_esteem()
    {
        return (int)sqrt(var_esteem());
    }
};