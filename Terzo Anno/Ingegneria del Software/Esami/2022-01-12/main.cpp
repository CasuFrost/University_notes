#include "utils.hpp"
#include "dtmc.hpp"
#include "monitor.cpp"
#include "env.cpp"
#include "client.cpp"
#include "drone.cpp"
#include <unistd.h>
void ex1()
{
    vector<vector<double>> edge_prob;
    vector<int> states;
    for (int i = 0; i < 6; i++)
    {
        states.push_back(i);
        vector<double> row(6, 0);
        edge_prob.push_back(row);
    }
    /*assegnazione probabilità*/
    {
        edge_prob[0][0] = (double)1 - ((double)1 / (double)(180 + MyMagicNumber));
        edge_prob[0][1] = (double)1 / (double)(180 + MyMagicNumber);
        edge_prob[1][1] = (double)1 - ((double)1 / (double)(90 + MyMagicNumber));
        edge_prob[1][2] = (double)1 / (double)(90 + MyMagicNumber);
        edge_prob[2][2] = (double)1 - ((double)1 / (double)(90 + MyMagicNumber));
        edge_prob[2][3] = (double)1 / (double)(90 + MyMagicNumber);
        edge_prob[3][3] = (double)1 - ((double)1 / (double)(60 + MyMagicNumber));
        edge_prob[3][4] = (double)1 / (double)(60 + MyMagicNumber);
        edge_prob[4][4] = (double)1 - ((double)1 / (double)(30 + MyMagicNumber));
        edge_prob[4][5] = (double)1 / (double)(30 + MyMagicNumber);
        edge_prob[5][5] = 1;
    }
    DTMC processo(states, edge_prob);
    vector<int> days_for_project;
    for (int i = 0; i < HORIZON; i++)
        days_for_project.push_back((int)processo.simulate_process(3));
    cout << "Valore atteso tempo di completamento:  " << avg_buffer(days_for_project) << "\n";
}

void ex2()
{
    Env env;
    Monitor monitor;
    for (int i = 0; i < 10000; i++)
    {

        monitor.time_step(env.time_step(i));
    }
    cout << "Valore atteso tempo fra due richieste: " << avg_buffer(monitor.time_gaps) << "\n";
}

void ex3()
{
    Client clientOdd(1);
    Client clientEven;
    Server server;

    Env env;
    for (int i = 0; i < 10000; i++)
    {
        Request r = env.time_step(i);
        clientEven.time_step(r, &server);
        clientOdd.time_step(r, &server);
        server.time_step(i);
    }
}

void ex5(int pyhton = 0)
{
    Drone drone;
    double ref = 500 + MyMagicNumber;
    double u;
    double prop_gain = 0.5;
    double der_gain = 1;
    double z_old = drone.z;
    vector<double> x_axis;
    vector<double> y_axis;
    int domain = 16000;
    for (int i = 0; i < domain; i++)
    {
        x_axis.push_back(i);
        y_axis.push_back(drone.z);
        /*strategia di controllo*/
        drone.time_step(u);
        double derivata = (drone.z - z_old) / T;
        double e = ref - drone.z;
        /*considero un controllore PD*/
        u = g + prop_gain * e - derivata * der_gain;
        z_old = drone.z;
    }
    ofstream data("plot.py");
    data << "import matplotlib.pyplot as plt\nimport numpy as np\nxpoints = ";
    data << "[";
    for (int i = 0; i < domain; i++)
    {
        data << x_axis[i];
        if (i != domain - 1)
            data << ",";
    }
    data << "]";
    data << "\nypoints =[";
    for (int i = 0; i < domain; i++)
    {
        data << y_axis[i];
        if (i != domain - 1)
            data << ",";
    }
    data << "]\n";
    data << "xaxis2=[0," << domain << ",]\n";
    data << "yaxis2=[" << ref << "," << ref << "]\n";
    data << "plt.ylabel('drone z-position')\n";
    data << "plt.xlabel('seconds*" << T << "')\n";
    data << "plt.plot(xaxis2, yaxis2)\n";
    data << "plt.plot(xpoints, ypoints)\nplt.show()";
    data.close();
    if (pyhton)
    {
        system("python3 plot.py");
    }
}

int main(int argc, char **argv)
{
    setvbuf(stdout, NULL, _IONBF, 0);
    srand((unsigned)time(NULL));
    ex5(1);
    exit(0);
    cout << "Ex 1\n";
    ex1();
    cout << "\nEx 2\n";
    ex2();
    ex5(1);
}