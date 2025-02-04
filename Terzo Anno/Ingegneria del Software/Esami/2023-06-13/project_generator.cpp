#include "utils.hpp"
#ifndef PROJECT_GEN_CPP
#define PROJECT_GEN_CPP
class ProjectGenerator
{
    double prob_to_gen = (double)1 - (double)1 / (double)A;

public:
    int time_step()
    {
        if (rand_float_0_1() < prob_to_gen)
        {
            return randi_range(1, 1000);
        }
        return 0;
    }
};
#endif