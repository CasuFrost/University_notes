#include "utils.hpp"

#ifndef ENV_HPP
#define ENV_HPP

class Env
{
private:
public:
    Env() {}
    Request time_step() /*ritorna una richiesta (-1,-1) se non è stata generata*/
    {
        if (rand_float_0_1() <= PROB_REQUEST)
        {
            Request r;
            r.f = randi_range(1, F2);
            r.id = randi_range(1, N2);
            return Request(randi_range(1, N2), randi_range(1, F2));
        }
        Request r;
        r.f = -1;
        r.id = -1;
        return r;
    }
};

#endif