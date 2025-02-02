#include "utils.hpp"

#ifndef ENV_CPP
#define ENV_CPP
class Env
{
public:
    Request time_step(int time)
    {
        if (rand_float_0_1() < (double)1 / ((double)30 + (double)MyMagicNumber))
        {
            return Request(randi_range(1, N), randi_range(1, M), time);
        }
        return Request(0, 0, 0);
    }
};

#endif