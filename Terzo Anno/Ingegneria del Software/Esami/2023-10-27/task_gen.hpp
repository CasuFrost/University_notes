#include "utils.hpp"
#include "task.hpp"
#include <unistd.h>
#ifndef TASK_GEN_HPP
#define TASK_GEN_HPP
class TaskGenerator
{
private:
    int first_task = 1;
    Task last_task;
    int time = 0;

public:
    TaskGenerator()
    {
    }
    int time_step(vector<Task> *buffer)
    {
        time++;
        Task next;
        if (rand_float_0_1() < p)
        {
            if ((*buffer).size() == B)
            {
                return 1;
            }
            /*selezione di una qualifica a random*/
            int random_qual = randi_range(1, Q);

            /*il primo task da generare è sempre identico*/
            if (first_task)
            {
                first_task = 0;
                next = Task(1, 1, random_qual, time);
                last_task = next;
                (*buffer).push_back(next);
            }
            else if (last_task.phase < N)
            {
                next = Task(last_task.project.id, last_task.phase + 1, random_qual, last_task.project.start);
                last_task = next;
                (*buffer).push_back(next);
            }
            else
            {
                next = Task(last_task.project.id + 1, 1, random_qual, time);
                last_task = next;
                (*buffer).push_back(next);
            }
        }
        return 0;
    }
};
#endif