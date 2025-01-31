#include "utils.cpp"
#include "dtmc.cpp"
#include "server.cpp"
#include "worker.cpp"
#include "job_generator.cpp"
#define HORIZON 1000

double ex2_simulation(int load_balancing = 0)
{
    vector<Worker> workers;
    for (int i = 0; i < W; i++)
    {
        workers.push_back(Worker(i));
    }
    Dispatcher dispatcher;
    Server server(workers);
    DeliveryManager deliveryManager;
    JobGenerator jobGenerator;

    while (true)
    {
        jobGenerator.time_step(&dispatcher);
        if (dispatcher.time_step(&server, load_balancing))
        {
            break;
        }
        if (server.time_step(&deliveryManager, load_balancing))
        {
            break;
        }
        if (deliveryManager.time_step())
        {
            break;
        }
    }
    /*for (int i = 0; i < W; i++)
    {
        cout << "worker " << i << " numero medio task nel buffer: " << (int)avg_buffer(server.workers[i].task_buffer_size_in_time) << "\n";
    }*/

    return deliveryManager.avg_completation_time();
}

void ex3(int load_balancing = 0)
{
    vector<vector<double>> real_avg(W);
    for (int o = 0; o < HORIZON; o++)
    {
        vector<Worker> workers;
        for (int i = 0; i < W; i++)
        {
            workers.push_back(Worker(i));
        }
        Dispatcher dispatcher;
        Server server(workers);
        DeliveryManager deliveryManager;
        JobGenerator jobGenerator;
        for (int k = 0; k < HORIZON; k++)
        {
            jobGenerator.time_step(&dispatcher);
            if (dispatcher.time_step(&server, load_balancing))
            {
                break;
            }
            if (server.time_step(&deliveryManager, load_balancing))
            {
                break;
            }
            if (deliveryManager.time_step())
            {
                break;
            }
        }
        for (int i = 0; i < W; i++)
        {
            real_avg[i].push_back(avg_buffer(server.workers[i].task_buffer_size_in_time));
        }
    }
    for (int i = 0; i < W; i++)
    {
        cout << "i=" << i << ", b=" << avg_buffer(real_avg[i]) << ", s=" << stdev_buffer(real_avg[i]) << "\n";
    }
}

void ex5() { ex3(1); }

void ex2()
{
    vector<double> avg;
    for (int i = 0; i < HORIZON; i++)
    {
        avg.push_back(ex2_simulation());
    }
    cout << "V=" << (int)avg_buffer(avg) << ", S=" << (int)stdev_buffer(avg);
}

void ex4()
{
    vector<double> avg;
    for (int i = 0; i < HORIZON; i++)
    {
        avg.push_back(ex2_simulation(1));
    }
    cout << "V=" << (int)avg_buffer(avg) << ", S=" << (int)stdev_buffer(avg);
}

int main()
{
    srand((unsigned)time(NULL));
    cout << "HORIZON = " << HORIZON << "\n\n";
    cout << "ESERCIZIO 2\n";
    ex2();
    cout << "\n";
    cout << "-------------------------------------\nESERCIZIO 3\n";
    ex3();
    cout << "-------------------------------------\nESERCIZIO 4\n";
    ex4();
    cout << "\n";
    cout << "-------------------------------------\nESERCIZIO 5\n";
    ex5();
}

/*
double ex3_simulation()
{
    Dispatcher dispatcher;
    vector<Server> servers;
    for (int i = 0; i < Q; i++)
    {
        vector<Worker> workers;
        for (int i = 0; i < W; i++)
        {
            workers.push_back(Worker(i));
        }
        Server server(workers);
        servers.push_back(server);
    }
    DeliveryManager deliveryManager;
    JobGenerator jobGenerator;

    for (int k = 0; k < HORIZON; k++)
    {
        jobGenerator.time_step(&dispatcher);
        int check = 0;
        for (int i = 0; i < Q; i++)
        {
            check += dispatcher.time_step(&(servers[i]));
        }
        if (check != 0)
            break;
        check = 0;
        for (int i = 0; i < Q; i++)
        {
            check += servers[i].time_step(&deliveryManager);
        }
        if (check != 0)
            break;
        if (deliveryManager.time_step())
        {
            break;
        }
    }
    return deliveryManager.avg_completation_time();
}

void ex3()
{
    vector<double> avg;
    for (int i = 0; i < HORIZON; i++)
    {
        avg.push_back(ex3_simulation());
    }
    cout << "V=" << (int)avg_buffer(avg) << ", S=" << (int)stdev_buffer(avg);
}
*/