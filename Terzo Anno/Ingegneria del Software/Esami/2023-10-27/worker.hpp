#include "taskGenerator.hpp"
const double EULER = 2.71828182845904523536;
class Worker
{
private:
    double trans_probability()
    {
        return 0.5 * pow(EULER, -(identifier / W) - (currTask.k / N) - (currTask.q / Q));
    }

public:
    int W;
    int N;
    int Q;
    int identifier;
    int qual;
    Task currTask;
    int state = 0;

    Worker(int W, int N, int Q, int identifier, int qual)
    {
        this->W = W;
        this->N = N;
        this->Q = Q;
        this->identifier = identifier;
        this->qual = qual;
    }

    void time_step(DeliveryManager *d_man)
    {
        if (DEBUG)
            cout << "worker " << identifier << " state : " << state;
        if (state != 0)
        {
            double p = trans_probability();
            if (DEBUG)
                cout << " current task : " << "(" << currTask.v << ", " << currTask.k << ", " << currTask.q << ")";
            double random_number = ((double)rand() / (double)RAND_MAX);
            if (random_number <= p)
            {
                state = 0;
                if (DEBUG)
                    cout << " TASK TERMINATO\n";
                if (currTask.k == N)
                {
                    /*Progetto completato*/
                    (*d_man).project_complete(currTask.v);
                }
                return;
            }
        }
        if (DEBUG)
            cout << "\n";
    }
};