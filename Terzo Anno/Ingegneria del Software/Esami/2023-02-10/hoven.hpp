#include "utils.hpp"

#ifndef HOVEN_HPP
#define HOVEN_HPP

class Oven
{
public:
    int d;
    Oven() { d = randi_range(0, d_max); }
    double x = 0;
    double x1 = 0;
    double second_passed = 0;
    void time_step(double u, double s)
    {
        x1 = x;
        second_passed += s;

        if ((int)second_passed == Td)
        {
            d = randi_range(0, d_max);
            second_passed = 0;
        }
        x += ((double)A5 * ((double)fmin(1, fmax(0, u))) - (double)B - (double)d) * T;
    }
};

#endif