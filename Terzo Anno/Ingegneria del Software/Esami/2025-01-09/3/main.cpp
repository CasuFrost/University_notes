#include "../monitor.hpp"
#define HORIZON 1000000
int main()
{
    Customer customer("parameters.txt");
    Monitor monitor;
    for (int i = 0; i < HORIZON; i++)
    {
        monitor.simulate_step(customer.simulate_step());
    }
    ofstream file("output.txt");
    file << "2025-01-09-Marco-Casu-2046212\n"
         << "Avg " << monitor.avg_esteem() << "\nStdDev " << monitor.stdev_esteem();
    file.close();
}