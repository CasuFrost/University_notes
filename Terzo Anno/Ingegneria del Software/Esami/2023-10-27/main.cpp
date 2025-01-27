#include "projectManager.hpp"
using namespace std;
int main()
{
    int N = 5;
    int Q = 5;
    double p = 0.2;
    int W = 5;
    int B = 50;
    srand((unsigned)time(NULL));
    setvbuf(stdout, NULL, _IONBF, 0);

    TaskGenerator t_gen(p, Q, N);
    ProjectManager p_man;
    vector<Task> taskBuffer;
    vector<vector<Worker>> workers;

    DeliveryManager d_man;

    /*generate workers*/
    for (int i = 0; i < Q; i++)
    {
        vector<Worker> tmp;

        for (int j = 0; j < W; j++)
        {
            Worker w(W, N, Q, (i * Q) + j, i);
            tmp.push_back(w);
        }
        workers.push_back(tmp);
    }

    for (int k = 0; k < 10000; k++)
    {
        if (DEBUG)
            cout << "\nTIME : " << k << "\n";
        t_gen.time_step(&taskBuffer, &d_man, k);
        if (taskBuffer.size() > B)
        {
            if (DEBUG)
                cout << "Simulazione interrotta : dimensioni buffer eccedute oppure nulle\n";
            exit(0);
        }
        //*worker
        for (int i = 0; i < Q; i++)
        {
            for (int j = 0; j < W; j++)
            {
                workers[i][j].time_step(&d_man);
            }
        }
        if (DEBUG)
            cout << "\nBUFFER : ";
        for (int i = 0; i < taskBuffer.size(); i++)
        {
            taskBuffer[i].print();
            if (DEBUG)
                cout << "  ";
        }
        p_man.time_step(&workers, &taskBuffer);
        if (DEBUG)
            cout << "\n-----------------------------------------\n\n";
    }
    cout << d_man.project_and_starting_times.size();
}