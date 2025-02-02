#include "utils.hpp"
#ifndef SERVER_CPP
#define SERVER_CPP
class Server
{
private:
    vector<Request> database;
    int deleting_period = 10;

public:
    int receive_request(Request r)
    {
        if (database.size() == 0)
        {
            database.push_back(r);
            return 1;
        }
        for (int i = 0; i < database.size(); i++)
        {
            if (database[i].m == r.m && database[i].n == r.n)
            {
                return 2;
            }
        }
        database.push_back(r);
        return 1;
    }

    void time_step(int time)
    {
        if (time % deleting_period == 0)
        {
            while (1)
            {
                int ret = 1;
                for (int i = 0; i < database.size(); i++)
                {
                    if (time - database[i].generation_time > 500)
                    {
                        // cout << "è l'istante " << time << " e scarto una richiesta generata nell'istante " << database[i].generation_time << "\n";
                        database.erase(database.begin() + i);
                        ret = 0;
                        break;
                    }
                }
                if (ret)
                {
                    return;
                }
            }
        }
    }
};
#endif