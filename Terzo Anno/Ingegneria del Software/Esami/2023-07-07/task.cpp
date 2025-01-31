#include "utils.cpp"
#ifndef TASK_CPP
#define TASK_CPP
class Task
{
public:
    int job;
    int phase;
    int start;
    int end;
    Task()
    {
    }
    Task(int v, int k)
    {
        phase = k;
        job = v;
    }
};
#endif