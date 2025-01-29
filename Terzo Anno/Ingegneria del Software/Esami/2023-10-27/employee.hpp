#include "utils.hpp"
#include "task.hpp"
#include "delivery_manager.hpp"
#ifndef EMPLOYEE_HPP
#define EMPLOYEE_HPP

class Employee
{
private:
    int time = 0;
    int working_time = 0;

public:
    double prob_to_step(int k)
    {
        double exp_arg = (-1) * ((employee_id / W) + (k / N) + (qual / Q));
        return 0.5 * (exp(exp_arg));
    }

    int employee_id;
    int qual; // qualifica del dipendente
    Task current_task;
    Employee(int q, int id)
    {
        qual = q;
        current_task = Task(0, 0, 0, 0);
        employee_id = id;
    }
    void time_step(DeliveryManager *deliveryManager)
    {
        time++;
        if (current_task.phase != 0)
        {
            working_time++;
            /*dipendente non in idle*/
            double rand = rand_float_0_1();
            if (rand >= prob_to_step(current_task.phase))
            {
                /*task terminato*/
                if (current_task.phase == N)
                {
                    /*progetto terminato*/
                    current_task.project.end = time;
                    (*deliveryManager).add_project(current_task.project);
                    /*consegna al delivery manager*/
                }
                current_task = Task(0, 0, 0, 0);
            }
        }
    }

    double working_time_perc() { return (double)working_time / (double)time; }
};

#endif