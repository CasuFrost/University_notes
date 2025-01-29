#include "utils.hpp"
#include "server.hpp"
#ifndef DISPATCHER_HPP
#define DISPATCHER_HPP

/*questa classe riceve richieste e le distribuisce ai Q server modellati con dei monitor*/
class Dispatcher
{
public:
    void time_step(Request request, int time, vector<Server> *servers)
    {
        if (request.id != -1)
        {
            /*una richiesta è stata ricevuta e va distribuita ad uno dei server*/
            TimeRequest tr;
            tr.arrive_time = time;
            tr.r = request;
            (*servers)[randi_range(0, Q - 1)].addRequest(tr);
        }
    }
};

#endif