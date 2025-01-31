#include "utils.cpp"
#include "task.cpp"
#include "worker.cpp"
#include "server.cpp"
#ifndef DISPATCHER_CPP
#define DISPATCHER_CPP
class Dispatcher
{
public:
    vector<int> jobs;
    int counter = 0;
    int time = 1;
    int time_step(Server *server, int load_balancing = 0)
    {
        if (jobs.size() > B)
        {
            return 1;
        }
        counter++;
        if (counter == D && jobs.size() > 0)
        {
            counter = 0;
            Task t(jobs[0], 1);
            t.start = time;
            jobs.erase(jobs.begin());
            if (load_balancing == 0)
            {
                (*server).workers[randi_range(0, (*server).workers.size() - 1)].task.push_back(t);
            }
            else
            {
                int best_worker_index = 0;
                for (int i = 0; i < W; i++)
                {
                    if ((*server).workers[i].task.size() < (*server).workers[best_worker_index].task.size())
                    {
                        best_worker_index = i;
                    }
                }
                (*server).workers[best_worker_index].task.push_back(t);
            }
            /*assegna al worker*/
        }
        time++;
        return 0;
    }
};
#endif