#include "utils.hpp"

class Task
{
public:
    int v;
    int k;
    int q;
    Task(int v, int k, int q)
    {
        this->v = v;
        this->k = k;
        this->q = q;
    }
    Task() {};

    void print()
    {
        if (DEBUG)
            cout << "(" << v << ", " << k << ", " << q << ")";
    }
};