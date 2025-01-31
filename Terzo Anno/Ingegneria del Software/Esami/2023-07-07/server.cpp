
#include "utils.cpp"
#include "task.cpp"
#include "worker.cpp"
using namespace std;

#ifndef SERVER_HPP
#define SERVER_HPP
class Server
{
public:
    vector<Worker> workers;
    Server(vector<Worker> w)
    {
        workers = w;
    }
    int time_step(DeliveryManager *deliveryManager, int load_balancing = 0)
    {
        int check = 0;
        for (int i = 0; i < W; i++)
        {
            check += workers[i].time_step(&workers, deliveryManager, load_balancing);
        }
        return check;
    }
};
#endif