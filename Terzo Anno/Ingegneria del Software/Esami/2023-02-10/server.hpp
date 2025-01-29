#include "utils.hpp"

#ifndef SERVER_HPP
#define SERVER_HPP

class TimeRequest
{
public:
    int arrive_time;
    Request r;
    int time_to_resolve = RHO;
    TimeRequest() {}
};

class Server
{
private:
    vector<TimeRequest> request;

public:
    vector<int> time_to_response;
    int received_req = 0;
    void time_step(int time)
    {
        if (request.size() != 0)
        {
            if (request[0].time_to_resolve == 0)
            {
                /*richiesta soddisfatta*/
                time_to_response.push_back(time - request[0].arrive_time);
                request.erase(request.begin());
            }
            else
            {
                request[0].time_to_resolve -= 1;
            }
        }
    }
    void addRequest(TimeRequest tr)
    {
        received_req++;
        request.push_back(tr);
    }

    double load_balance()
    {
        return (double)received_req / (double)HORIZON;
    }
};

#endif