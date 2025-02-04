#include "monitor.hpp"

class Dispatcher
{
private:
    int num_customer;

    vector<int> global_list;

public:
    vector<vector<int>> message_list;
    Dispatcher(int n)
    {
        num_customer = n;
        for (int i = 0; i < n; i++)
        {
            vector<int> tmp;
            message_list.push_back(tmp);
        }
    }

    void simulate_step(vector<int> request, int time)
    {
        for (int req = 0; req < request.size(); req++)
        {
            if (request[req])
            {
                message_list[req].push_back(time);
                global_list.push_back(time);
            }
        }
    }

    int check_order_preservation()
    {
        for (int i = 1; i < global_list.size(); i++)
        {
            if (global_list[i] < global_list[i - 1])
            {
                return 0;
            }
        }
        return 1;
    }

    void print_global_list()
    {
        cout << "Global List:\n";
        for (int elem : global_list)
        {
            cout << elem << " ";
        }
        cout << "\n";
    }

    void print_message_list()
    {
        for (int i = 0; i < message_list.size(); i++)
        {
            cout << "\ncustomer " << i << " :\n";
            for (int j = 0; j < message_list[i].size(); j++)
            {
                cout << "     message at time " << message_list[i][j] << "\n";
            }
        }
    }
};