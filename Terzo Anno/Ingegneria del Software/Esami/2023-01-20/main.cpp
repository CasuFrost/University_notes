#include "env.cpp"
#include <unistd.h>

void ex5()
{
    double second_passed = 0;
    double g = 9.8;
    double w1 = (double)1 - (double)2 * rand_float_0_1();
    double w2 = (double)1 - (double)2 * rand_float_0_1();
    double r1 = 30;
    double r2 = 30;
    double r3 = 30;
    double x1 = 0;
    double x2 = 0;
    double x3 = 0;
    double k1 = 1;
    double k2 = 1;
    double u1 = 0;
    double u2 = 0;
    double u3 = 0;
    vector<double> error1;
    vector<double> error2;
    vector<double> error3;
    for (int t = 0; t < HORIZON; t++)
    {
        if (DEBUG)
        {
            system("clear");
            // cout << "x1: " << x1 << "     x2: " << x2 << "    x3: " << x3 << "\n";
            for (int i = 0; i < 50; i++)
            {
                for (int j = 0; j < 60; j++)
                {
                    if (i == (int)r1 && j == (int)r2)
                    {
                        cout << "[OBIETTIVO]";
                    }
                    else if (i == (int)x1 && j == (int)x2)
                    {
                        cout << "[DRONE]";
                    }
                    else
                    {
                        cout << " ";
                    }
                }
                cout << "\n";
            }
            usleep(30);
        }

        second_passed += T;
        if (second_passed == Tw) /*effetti esogeni*/
        {
            w1 = (double)1 - (double)2 * rand_float_0_1();
            w2 = (double)1 - (double)2 * rand_float_0_1();
            second_passed = 0;
        }

        /*calcolo controllo*/
        u1 = k1 * (r1 - x1);
        u2 = k1 * (r2 - x2);
        u3 = k1 * (r3 - x3) + g;

        /*dinamica del sistema, controllo proporzionale*/
        x1 += (double)T * (u1 + w1);
        x2 += (double)T * (u2 + w2);
        x3 += (double)T * (u3 - g);
        error1.push_back(r1 - x1);
        error2.push_back(r2 - x2);
        error3.push_back(r3 - x3);
    }
    ofstream file("output/outputs5.txt");
    file << "ComponenteIndex AvgErr StdDevErr\n";
    file << "1 " << avg_buffer(error1) << " " << stdev_buffer(error1) << "\n";
    file << "2 " << avg_buffer(error2) << " " << stdev_buffer(error2) << "\n";
    file << "3 " << avg_buffer(error3) << " " << stdev_buffer(error3);
    file.close();
}

int main()
{
    setvbuf(stdout, NULL, _IONBF, 0);
    srand((unsigned)time(NULL));

    Monitor monitor;
    Env env;
    Dispatcher disp;
    for (int i = 0; i < HORIZON; i++)
    {
        env.time_step(&disp, &monitor, i);
        disp.time_step(i, &monitor);
    }
    ofstream file("output/outputs2.txt");
    file << "Avg1 StdDev1 Avg2 StdDev2 Avg3 StdDev3 AvgWait StdWait\n";
    file << monitor.avg_request().a << " " << monitor.stddev_request().a << " " << monitor.avg_request().b << " " << monitor.stddev_request().b << " " << monitor.avg_request().id << " " << monitor.stddev_request().id << " " << (int)monitor.avg_wait() << " " << (int)monitor.stddev_wait();

    disp.calc_load_balancing();
    file.close();
    file.open("output/outputs3.txt");
    ofstream file2("output/outputs4.txt");

    for (int i = 0; i < K; i++)
    {
        file2 << i << " " << disp.load_balancing[i] << "\n";
        file << i << " " << avg_buffer(monitor.output_request_time[i]) << " " << stdev_buffer(monitor.output_request_time[i]) << "\n";
    }
    file.close();
    file2.close();

    ex5();
}