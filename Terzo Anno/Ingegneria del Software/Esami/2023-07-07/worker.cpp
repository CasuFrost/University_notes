#include "utils.cpp"
#include "task.cpp"
#include "delivery_manager.cpp"
#ifndef WORKER_CPP
#define WORKER_CPP
class Worker
{
public:
    vector<int> task_buffer_size_in_time;
    vector<Task> task;
    Task current_task;
    int state = 0;
    int time = 1;
    int identifier;
    Worker(int i)
    {
        identifier = i;
    }
    int time_step(vector<Worker> *workers, DeliveryManager *deliveryManager, int load_balancing = 0)
    {
        task_buffer_size_in_time.push_back(task.size());
        if (task.size() > B)
        {
            return 1;
        }
        if (state == 0 && task.size() > 0)
        {
            state = task[0].phase;
            current_task = task[0];
            task.erase(task.begin());
        }
        if (state != 0)
        {
            double prob = 0.5 * exp(-((double)identifier / (double)W) - ((double)state / (double)N));

            if (rand_float_0_1() >= prob)
            {
                if (state == N)
                {
                    current_task.end = time;
                    (*deliveryManager).completed.push_back(current_task);
                }
                else
                {
                    Task new_task(current_task.job, state + 1);
                    new_task.start = current_task.start;
                    /*criterio di assegnazione*/
                    if (load_balancing == 0)
                    {
                        (*workers)[randi_range(0, (*workers).size() - 1)].task.push_back(new_task);
                    }
                    else
                    {
                        int best_worker_index = 0;
                        for (int i = 0; i < W; i++)
                        {
                            if ((*workers)[i].task.size() < (*workers)[best_worker_index].task.size())
                            {
                                best_worker_index = i;
                            }
                        }
                        (*workers)[best_worker_index].task.push_back(new_task);
                    }
                }
                state = 0;
            }
        }
        time++;
        return 0;
    }
    void log()
    {
        cout << task_buffer_size_in_time.size();
    }
};
#endif