#include "utils.hpp"
#ifndef DELIVERY_MAN_CPP
#define DELIVERY_MAN_CPP

class DeliveryManager
{
    vector<Task> task_buffer;
    vector<int> durations;

public:
    int time_step()
    {
        if (task_buffer.size() > B)
        {
            return 1;
        }
        if (task_buffer.size() > 0)
            task_buffer.erase(task_buffer.begin());
        return 0;
    }
    void add_task(Task t)
    {
        task_buffer.push_back(t);
        durations.push_back(t.duration);
    }
    double avg_project_duration()
    {
        if (durations.size() == 0)
        {
            return 0;
        }
        return avg_buffer(durations);
    }
    double stdev_project_duration()
    {
        if (durations.size() == 0)
        {
            return 0;
        }
        return stdev_buffer(durations);
    }
};

#endif