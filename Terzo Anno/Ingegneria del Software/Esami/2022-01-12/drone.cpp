#include "utils.hpp"
#ifndef DRONE_CPP
#define DRONE_CPP
class Drone
{
public:
    double z = 100 + MyMagicNumber;
    double v = 0;
    void time_step(double u)
    {
        v += (u - g) * T;
        z += v * T;
    }
};
#endif