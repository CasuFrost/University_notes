#include "../dtmc.cpp"

int get_cost()
{
    ifstream file("parameters.txt");
    string line;
    getline(file, line);
    vector<string> v = splitString(line);
    file.close();
    if (v[0] == "C")
    {
        return stoi(v[1]);
    }
    else
    {
        cout << "parameter error\n";
        exit(1);
    }
}

int main()
{

    DTMC processo("parameters.txt", 0, 1);

    ofstream file("output.txt");
    file << "2025-01-09-Marco-Casu-2046212\n"
         << "P " << processo.probability_max_cost(10000, get_cost(), 0);
    file.close();
}