#include "utils.hpp"
#include "delivery_manager.cpp"
#ifndef EMPLOYEE_CPP
#define EMPLOYEE_CPP
class Employee
{
private:
    Task current;
    int id;

public:
    vector<Task> task_buffer;
    vector<int> task_number;

    Employee(int id)
    {
        this->id = id;
        current.project = 0;
    }
    void add_task(Task t)
    {
        task_buffer.push_back(t);
    }

    int time_step(int time, vector<Employee> *employees, DeliveryManager *deliveryManager, int load_balancing = 0)
    {
        if (task_buffer.size() > B)
        {
            /*dimensioni buffer eccedute*/
            return 1;
        }
        if (current.project == 0)
        {
            if (task_buffer.size() != 0)
            {
                current = task_buffer[0];
                task_buffer.erase(task_buffer.begin());
            }
        }
        else
        {
            double prob = 0.5 * (exp(-((double)id / (double)W) - ((double)current.phase / (double)N)));
            if (rand_float_0_1() >= prob)
            {
                /*Termina task*/

                /*manda al delivery o ad un dipendente*/
                if (current.phase < N)
                {
                    if (load_balancing == 1)
                    {
                        /*cerca il dipendente più scarico*/
                        int index = 0;
                        for (int i = 0; i < W; i++)
                        {
                            if ((*employees)[i].task_buffer.size() < (*employees)[index].task_buffer.size())
                            {
                                index = i;
                            }
                        }
                        (*employees)[index].add_task(Task(current.project, current.phase + 1, current.start));
                    }
                    else if (load_balancing == 2)
                    {
                        int index = 0;
                        for (int i = 0; i < W; i++)
                        {
                            if ((*employees)[i].expected_completation_time() < (*employees)[index].expected_completation_time())
                            {
                                index = i;
                            }
                        }
                        (*employees)[index].add_task(Task(current.project, current.phase + 1, current.start));
                    }
                    else
                    {
                        (*employees)[randi_range(0, (*employees).size() - 1)].add_task(Task(current.project, current.phase + 1, current.start));
                    }
                }
                else
                {
                    Task t(current.project, current.phase, current.start);
                    t.duration = time - current.start;
                    (*deliveryManager).add_task(t);
                }

                /*torna nello stato 0*/
                current = Task(0, 0, 0);
            }
        }
        task_number.push_back(task_buffer.size());
        return 0;
    }
    double avg_buffer_size() { return avg_buffer(task_number); }
    double stdev_buffer_size() { return stdev_buffer(task_number); }

    double expected_completation_time()
    {
        double expected_value = 0;
        for (int i = 0; i < task_buffer.size(); i++)
        {
            double prob = 0.5 * (exp(-((double)id / (double)W) - ((double)task_buffer[i].phase / (double)N)));
            double ex_val_task = (double)1 / ((double)1 - prob);
            expected_value += ex_val_task;
        }
        return expected_value;
    }
};
#endif