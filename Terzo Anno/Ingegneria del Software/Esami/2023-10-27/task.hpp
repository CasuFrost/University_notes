#include "utils.hpp"
#ifndef TASK_HPP
#define TASK_HPP

class Project
{
public:
    int start;
    int end;
    int id;
    Project()
    {
    }
    Project(int id, int start)
    {
        this->id = id;
        this->start = start;
    }
};

class Task
{
private:
public:
    int phase;
    Project project;
    int requested_qual;
    Task() {}
    Task(int v, int k, int q, int time)
    {
        phase = k;
        project = Project(v, time);
        requested_qual = q;
    }
};

#endif