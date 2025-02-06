#include "utils.hpp"

#ifndef SERVER_CPP
#define SERVER_CPP
class TimedReq
{
public:
    int r;
    int time;
    void decr()
    {
        time--;
    }
};
class Server
{
private:
    int time = 0;
    int last_req_served = 0;
    vector<TimedReq> request;
    double t1;
    double t2;

public:
    int req_in_buffer = 0;
    vector<int> element_in_buffer;
    int served_customer = 0;
    Server(double t1, double t2)
    {
        this->t1 = t1;
        this->t2 = t2;
    }
    void add_request(int a)
    {
        TimedReq r;
        r.r = a;
        r.time = 0;
        if (a == 1)
        {
            r.time = round(t1);
        }
        else if (a == 2)
        {
            r.time = round(t2);
        }
        request.push_back(r);
    }
    void time_step()
    {
        element_in_buffer.push_back(req_in_buffer);
        while (request.size() != 0 && request[0].r == 0)
        {
            if (last_req_served == 1)
            {
                served_customer++;
                last_req_served = 0;
            }
            request.erase(request.begin());
        }
        if (request.size() != 0)
        {
            if (request[0].time == 0)
            {
                /*RICHIESTA SERVITA*/
                request.erase(request.begin());
                last_req_served = 1;
                req_in_buffer--;
            }
            else
            {
                request[0].time = request[0].time - 1;
            }
        }
        time++;
    }
};

#endif