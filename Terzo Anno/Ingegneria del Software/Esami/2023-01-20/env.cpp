#include "utils.hpp"
#include "dispatcher.cpp"
#ifndef ENV_CPP
#define ENV_CPP
class Env
{
private:
public:
    Env() {}
    void time_step(Dispatcher *dispatcher, Monitor *monitor, int time)
    {
        /*il tempo medio fra una richiesta e l'altra è di 10
        unità di tempo, quindi la probabilità ad ogni time_step di
        generare una richiesta è di un decimo.*/
        if (rand_float_0_1() <= 0.1)
        {
            Request request(randi_range(-1000, 1000), randi_range(-1000, 1000), randi_range(-1000, 1000));
            (*dispatcher).input_queues[randi_range(0, N - 1)].push_back(request);
            (*monitor).add_request(request, time);
        }
    }
};
#endif