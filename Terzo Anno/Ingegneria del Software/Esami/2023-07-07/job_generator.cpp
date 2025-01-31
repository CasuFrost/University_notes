#include "utils.cpp"
#include "task.cpp"
#include "dispatcher.cpp"
#ifndef JOB_GEN_CPP
#define JOB_GEN_CPP
#define prob ((double)1 - (double)1 / (double)L)
class JobGenerator
{
public:
    void time_step(Dispatcher *d)
    {
        if (rand_float_0_1() < prob)
        {
            /*invia job a random al dispatcher*/
            (*d).jobs.push_back(randi_range(1, 100));
        }
    }
};
#endif