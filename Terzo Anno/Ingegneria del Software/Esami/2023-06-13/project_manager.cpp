#include "utils.hpp"
#include "employee.cpp"
#ifndef PROJECT_MAN_CPP
#define PROJECT_MAN_CPP
class ProjectManager
{
private:
    vector<int> project_buffer;

public:
    int time_step(int time, vector<Employee> *employees)
    {
        if (project_buffer.size() > B)
        {
            return 1;
        }
        if (project_buffer.size() != 0)
        {
            int pr = project_buffer[0];
            project_buffer.erase(project_buffer.begin());
            /*assegna a dipendente*/
            int a = randi_range(0, (*employees).size() - 1);
            // cout << a << "\n";
            (*employees)[a].add_task(Task(pr, 1, time));
        }
        return 0;
    }

    void add_project(int v)
    {
        if (v == 0)
        {
            return;
        }
        project_buffer.push_back(v);
    }
};
#endif