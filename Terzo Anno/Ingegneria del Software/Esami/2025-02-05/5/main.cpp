#include "dtmc.cpp"
#include "customer.cpp"
#include "server.cpp"
double simulation()
{
    srand((unsigned)time(NULL));
    setvbuf(stdout, NULL, _IONBF, 0);
    double t1;
    double t2;
    vector<vector<double>> edge_prob;
    for (int i = 0; i < 3; i++)
    {
        vector<double> row(3, 0);
        edge_prob.push_back(row);
    }
    ifstream file("parameters.txt");
    string line;
    getline(file, line);
    vector<string> tmp = splitString(line);
    double L;
    if (tmp[0] == "L")
    {
        L = stof(tmp[1]);
    }
    getline(file, line);
    tmp = splitString(line);
    while (tmp.size() == 3)
    {
        edge_prob[stoi(tmp[0])][stoi(tmp[1])] = stof(tmp[2]);
        getline(file, line);
        tmp = splitString(line);
    }
    t1 = stof(tmp[0]);
    getline(file, line);
    tmp = splitString(line);
    t2 = stof(tmp[0]);
    file.close();

    Customer customer(&edge_prob);

    Server server(t1, t2);
    for (int time = 0; time < H; time++)
    {
        int a = customer.time_step();

        if (a != 0)
        {
            server.req_in_buffer++;
        }
        server.add_request(a);

        server.time_step();
        // cout << "time " << time << " req " << server.req_in_buffer << "\n";
    }
    if (avg_buffer(server.element_in_buffer) > L)
        return 1;
    return 0;
}

int main(int argc, char **argv)
{
    srand((unsigned)time(NULL));
    setvbuf(stdout, NULL, _IONBF, 0);
    int num = 0;
    int steps = 1000;
    for (int i = 0; i < steps; i++)
    {
        num += simulation();
    }
    ofstream output("results.txt");
    output << "2025-02-05-marco-casu-2046212\n";

    output << "P " << (double)num / (double)steps;

    output.close();
    return 0;
}