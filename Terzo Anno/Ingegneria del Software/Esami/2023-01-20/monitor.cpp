#include "utils.hpp"
#ifndef MONITOR_CPP
#define MONITOR_CPP
class Monitor
{

    vector<Request> generated_request;
    vector<int> request_time;
    int output_last = 0;
    int input_last = 0;

public:
    vector<vector<int>> output_request_time;
    Monitor()
    {
        for (int i = 0; i < K; i++)
        {
            vector<int> r;
            output_request_time.push_back(r);
        }
    }

    void add_request(Request req, int time)
    {
        generated_request.push_back(req);
        request_time.push_back(time - input_last);
        input_last = time;
    }

    Request stddev_request()
    {
        if (generated_request.size() == 0)
        {
            cout << "Zero request arrived\n";
            return Request(1001, 1001, 1001);
        }
        vector<int> first_num;
        vector<int> second_num;
        vector<int> id;
        for (Request r : generated_request)
        {
            first_num.push_back(r.a);
            second_num.push_back(r.b);
            id.push_back(r.id);
        }
        return Request((int)stdev_buffer(first_num), (int)stdev_buffer(second_num), (int)stdev_buffer(id));
    }

    Request avg_request()
    {
        if (generated_request.size() == 0)
        {
            cout << "Zero request arrived\n";
            return Request(1001, 1001, 1001);
        }
        vector<int> first_num;
        vector<int> second_num;
        vector<int> id;
        for (Request r : generated_request)
        {
            first_num.push_back(r.a);
            second_num.push_back(r.b);
            id.push_back(r.id);
        }
        return Request((int)avg_buffer(first_num), (int)avg_buffer(second_num), (int)avg_buffer(id));
    }
    double avg_wait()
    {
        if (request_time.size() != 0)
        {
            return avg_buffer(request_time);
        }
        cout << "Zero request arrived\n";
        return -1;
    }
    double stddev_wait()
    {
        if (request_time.size() != 0)
        {
            return stdev_buffer(request_time);
        }
        cout << "Zero request arrived\n";
        return -1;
    }
    void add_output_request(int k, int time)
    {
        output_request_time[k].push_back(time - output_last);
        output_last = time;
    }
};
#endif