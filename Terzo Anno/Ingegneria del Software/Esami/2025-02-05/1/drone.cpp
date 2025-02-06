#include "utils.hpp"
#ifndef DRONE_CPP
#define DRONE_CPP
class Drone
{
private:
    double X1;
    double Y1;
    double X2;
    double Y2;

public:
    double x = 0;
    double y = 0;
    Drone(double X1, double Y1, double X2, double Y2)
    {
        this->X1 = X1;
        this->X2 = X2;
        this->Y1 = Y1;
        this->Y2 = Y2;
        double xmin = fmin(X1, X2);
        double xmax = fmax(X1, X2);
        double ymin = fmin(Y1, Y2);
        double ymax = fmax(Y1, Y2);
        x = randi_range(xmin, xmax) + 1 - 2 * rand_float_0_1(); // random start position
        y = randi_range(ymin, ymax) + 1 - 2 * rand_float_0_1();
        ; // random start position
        if (x < X1)
            x = X1;
        if (x > X2)
            x = X2;
        if (y < Y1)
            y = Y1;
        if (y > Y2)
            y = Y2;
        // cout << "start pos " << x << " " << y << "\n";
    }

    void time_step()
    {
        double vx = 0.5 - rand_float_0_1();
        double vy = 0.5 - rand_float_0_1();
        x = fmin(X2, fmax(X1, x + vx * (double)T));
        y = fmin(Y2, fmax(Y1, y + vy * (double)T));
        // cout << "pos : " << x << " " << y << "\n";
    }
};
#endif