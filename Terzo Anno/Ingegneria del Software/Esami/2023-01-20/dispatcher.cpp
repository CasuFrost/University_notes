#include "monitor.cpp"
#ifndef DISPATCHER_CPP
#define DISPATCHER_CPP

class Dispatcher
{
    int time_passed = 0;

public:
    vector<vector<Request>> input_queues;
    vector<vector<Request>> output_queues;
    vector<double> load_balancing;
    Dispatcher()
    {
        for (int i = 0; i < N; i++)
        {
            vector<Request> row;
            input_queues.push_back(row);
        }
        for (int i = 0; i < K; i++)
        {
            vector<Request> row;
            output_queues.push_back(row);
        }
    }
    void calc_load_balancing()
    {
        for (int i = 0; i < K; i++)
        {
            load_balancing.push_back((double)output_queues.size() / (double)time_passed);
        }
    }
    void time_step(int time, Monitor *monitor)
    {
        for (int i = 0; i < K; i++)
        {
            int index = randi_range(0, N - 1);
            if (input_queues[index].size() != 0)
            {
                output_queues[i].push_back(input_queues[index][0]);
                input_queues[index].erase(input_queues[index].begin());
                (*monitor).add_output_request(i, time);
            }
        }
        time_passed++;
    }
};
#endif

/*
cout << "istante: " << time << "\n";
for (int i = 0; i < N; i++)
{
    cout << "\nCODA " << i << " ";
    for (int j = 0; j < input_queues[i].size(); j++)
    {
        cout << "(" << input_queues[i][j].a << "," << input_queues[i][j].b << "," << input_queues[i][j].id << ") ";
    }
    cout << "\n";
}
*/