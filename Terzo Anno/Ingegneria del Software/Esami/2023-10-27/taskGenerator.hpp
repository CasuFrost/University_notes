#include "task.hpp"

class TaskGenerator
{
private:
    double p;
    Task lastTask;
    int Q;
    int N;
    int firstTask = 1;

public:
    TaskGenerator(double p, int Q, int N)
    {
        this->p = p;
        this->Q = Q;
        this->N = N;
    }

    void time_step(vector<Task> *buffer, DeliveryManager *d_man, int time)
    {
        double random_number = ((double)rand() / (double)RAND_MAX);
        // if(DEBUG) cout << random_number << " " << p << "\n";
        if (random_number <= p)
        {

            /*genera task*/
            if (firstTask)
            {
                firstTask = 0;
                int q = rand() % Q;
                Task t(1, 1, q);
                (*d_man).new_project(1, time);
                lastTask = t;
                if (DEBUG)
                    cout << "task generato: " << "(" << t.v << ", " << t.k << ", " << t.q << ")\n";
                (*buffer).push_back(t);
                return;
            }
            if (lastTask.k < N)
            {
                int q = rand() % Q;
                Task t(lastTask.v, lastTask.k + 1, q);
                (*buffer).push_back(t);
                if (DEBUG)
                    cout << "task generato: " << "(" << t.v << ", " << t.k << ", " << t.q << ")\n";
                lastTask = t;
            }
            else
            {
                int q = rand() % Q;
                Task t(lastTask.v + 1, 1, q);
                (*d_man).new_project(lastTask.v + 1, time);
                (*buffer).push_back(t);
                if (DEBUG)
                    cout << "task generato: " << "(" << t.v << ", " << t.k << ", " << t.q << ")\n";
                lastTask = t;
            }
        }
    }
};