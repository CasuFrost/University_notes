#include "utils.hpp"
#ifndef CONTROLLER_HPP
#define CONTROLLER_HPP
class Controller
{
public:
    double time_step(double x, double x1, double r)
    {
        return (double)k1 * (x - r) + ((double)(P * 2) / T) * (x - x1);
    }
};
#endif