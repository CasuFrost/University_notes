#include "../dispatcher.hpp"
#define HORIZON 1000000
int main()
{
    int customer_number;
    ifstream file("parameters.txt");
    string line;
    getline(file, line);
    file.close();
    vector<string> s = splitString(line);
    if (s[0] == "N")
    {
        customer_number = stoi(s[1]);
    }
    else
    {
        cout << "error parameter\n";
        return -1;
    }

    vector<Customer> customers;
    for (int i = 0; i < customer_number; i++)
    {
        customers.push_back(Customer("parameters.txt", 1));
    }
    Dispatcher dispatcher(customer_number);

    for (int i = 0; i < 100000; i++)
    {
        vector<int> request(customer_number, 0);
        for (int k = 0; k < customer_number; k++)
        {
            request[k] = customers[k].simulate_step();
        }
        dispatcher.simulate_step(request, i);
    }
    ofstream file_o("output.txt");
    file_o << "2025-01-09-Marco-Casu-2046212\n";
    for (int i = 0; i < customer_number; i++)
    {
        file_o << i << " " << dispatcher.message_list[i].size() << "\n";
    }
    file_o.close();
}