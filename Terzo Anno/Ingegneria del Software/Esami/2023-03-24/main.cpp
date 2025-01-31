#include "utils.hpp"
#include "dtmc.hpp"
#include <unistd.h>
#define T 1
#define HORIZON 1000
#define OUT cout
class Demand
{
public:
    Demand() {}
    double x = 0;
    void time_step()
    {
        x += (double)T * rand_float_min1_plus1();
    }
};

class Resource
{
public:
    Resource() {}
    double r = 1;
    void time_step(double u)
    {
        r = r * u;
    }
};

class Controller
{
public:
    Controller() {}
    double u = 1;
    double gain = 1;
    double time_step(double z)
    {
        double incr = u * 0.1;
        if (z > 0)
        {
            u += incr;
        }
        else if (z < 0)
        {
            u -= incr;
        }
        return u;
    }
};

void ex5()
{
}

int main()
{
    srand(time(NULL));
    Demand x;
    Resource r;
    Controller u;
    vector<double> r_values;
    vector<double> z_values;
    // double z = 0;
    for (int i = 0; i < HORIZON; i++)
    {
        double z = (exp(x.x) - r.r);
        if (DEBUG)
        {
            system("clear");
            cout << "x(t)= " << x.x << "    z(t)=" << z << "    r(t)=" << r.r << "\n";
            usleep(100000);
        }
        x.time_step();
        double control = u.time_step(z);
        r.time_step(control);

        r_values.push_back(r.r);
        z_values.push_back(z);
    }
    // cout << x.x;
    ofstream file("output.txt");
    OUT << "AvgErr1 StdDevErr1 AvgErr2 StdDevErr2\n";
    OUT << avg_buffer(z_values) << " ";
    OUT << stdev_buffer(z_values) << " ";
    OUT << avg_buffer(r_values) << " ";
    OUT << stdev_buffer(r_values);
    file.close();
}