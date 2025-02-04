#include "../dtmc.cpp"
int main()
{
    DTMC processo("parameters.txt");
    ofstream file("output.txt");
    file << "2025-01-09-Marco-Casu-2046212\n"
         << "C " << processo.expected_cost_mc_simulation(10000, 0);
    file.close();
}