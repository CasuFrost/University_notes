#include "utils.hpp"
#include "project_generator.cpp"
#include "project_manager.cpp"

void ex1(int lb = 0)
{
    ProjectGenerator projectGenerator;
    ProjectManager projectManager;
    vector<Employee> employees;
    DeliveryManager deliveryManager;
    for (int i = 0; i < W; i++)
    {
        employees.push_back(Employee(i + 1));
    }
    int check;

    /*Simulazione*/
    for (int time = 0; time < HORIZON; time++)
    {
        check = 0;
        /*generazione progetto*/
        projectManager.add_project(projectGenerator.time_step());

        check += projectManager.time_step(time, &employees);

        for (int i = 0; i < W; i++)
        {
            check += employees[i].time_step(time, &employees, &deliveryManager, lb);
        }
        check += deliveryManager.time_step();
        if (check != 0)
        {
            break;
        }
    }

    cout << "Avg " << (int)deliveryManager.avg_project_duration() << " Stddev " << (int)deliveryManager.stdev_project_duration() << "\n";
    if (lb != 2)
    {
        for (int i = 0; i < W; i++)
        {
            cout << "   dip " << i << setprecision(2) << " AvgBuffSize " << employees[i].avg_buffer_size() << " StddevBuffSize " << employees[i].stdev_buffer_size() << "\n";
        }
    }
}

int main(int argc, char **argv)
{
    srand(time(NULL));
    ex1();
    cout << "\n";
    ex1(1);
    cout << "\n";
    ex1(2);
}