#include "utils.cpp"
#include "task.cpp"
#ifndef DELIVERY_MAN_CPP
#define DELIVERY_MAN_CPP
class DeliveryManager
{
public:
    vector<Task> completed;
    void print_comp()
    {
        cout << "job completati:\n";
        for (int i = 0; i < completed.size(); i++)
        {
            cout << "   " << completed[i].job << "  entrato : " << completed[i].start << "  terminato :" << completed[i].end << "\n";
        }
    }
    int time_step()
    {
        if (completed.size() > B)
        {
            return 1;
        }
        return 0;
    }
    double avg_completation_time()
    {
        if (completed.size() == 0)
            return 0;
        vector<double> times;
        for (int i = 0; i < completed.size(); i++)
        {
            times.push_back(completed[i].end - completed[i].start);
        }
        return avg_buffer(times);
    }
};
#endif