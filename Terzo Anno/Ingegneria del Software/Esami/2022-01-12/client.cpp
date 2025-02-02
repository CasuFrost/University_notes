#include "utils.hpp"
#include "server.cpp"
#ifndef CLIENT_CPP
#define CLIENT_CPP
class Client
{
    int accept_odd;

public:
    Client(int ao = 0)
    {
        accept_odd = ao;
    }
    int time_step(Request request, Server *server)
    {
        if (request.m == 0)
            return -1;
        if ((accept_odd && request.n % 2 == 1) || (accept_odd == 0 && request.n % 2 == 0))
        {
            return (*server).receive_request(request);
        }
        return -1;
    }
};
#endif