#include "utils.hpp"
#ifndef MONITOR_CPP
#define MONITOR_CPP
class Monitor
{
public:
    vector<int> time_gaps;
    vector<Request> request_buffer;
    void time_step(Request r)
    {
        if (r.m != 0)
        {
            if (request_buffer.size() == 0)
            {
                time_gaps.push_back(r.generation_time);
            }
            else
            {
                time_gaps.push_back(r.generation_time - request_buffer[request_buffer.size() - 1].generation_time);
            }
            request_buffer.push_back(r);
        }
    }
};
#endif