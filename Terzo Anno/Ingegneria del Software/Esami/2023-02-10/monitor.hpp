#include "utils.hpp"

#ifndef MONITOR_HPP
#define MONITOR_HPP

class Monitor
{
private:
    vector<int> time_gaps;
    int last_time = 0;

public:
    void time_step(int time, Request r)
    {

        if (r.f != -1)
        {
            time_gaps.push_back(time - last_time);
            last_time = time;
        }
    }

    int avg_time_gap() { return avg_buffer(time_gaps); }
    int stddev_time_gap() { return stdev_buffer(time_gaps); }
};

#endif