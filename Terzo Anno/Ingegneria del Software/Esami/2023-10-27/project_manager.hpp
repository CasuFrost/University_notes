#include "utils.hpp"
#include "task.hpp"
#include "employee.hpp"
#ifndef PROJ_MAN_HPP
#define PROJ_MAN_HPP
class ProjectManager
{
private:
    int time = 0;
    void assign_task(vector<Task> *buffer, vector<Employee> *employees, int ex3 = 0)
    {
        vector<int> emp_index_buffer;
        Task element_to_assign = (*buffer)[0];
        for (int i = 0; i < (*employees).size(); i++)
        {
            int cond = (*employees)[i].qual == element_to_assign.requested_qual;
            if (ex3)
            {
                cond = (*employees)[i].qual == element_to_assign.requested_qual && (*employees)[i].current_task.phase == 0;
            }
            if (cond)
            {
                emp_index_buffer.push_back(i);
            }
        }

        if (emp_index_buffer.size() == 0)
        {
            return;
        }

        int i = randi_range(0, emp_index_buffer.size() - 1);

        if ((*employees)[emp_index_buffer[i]].current_task.phase != 0)
        {
            return;
        }

        if (DEBUG)
            cout << "Assegnato al dip. " << i << " con qualifca " << (*employees)[emp_index_buffer[i]].qual << " il task (" << (*buffer)[0].project.id << "," << (*buffer)[0].phase << "," << (*buffer)[0].requested_qual << ")\n";
        (*employees)[emp_index_buffer[i]].current_task = element_to_assign;
        buffer->erase(buffer->begin());

        return;
    }

    void assign_task_minimizing_wait_time(vector<Task> *buffer, vector<Employee> *employees)
    {
        /*Per come viene calcolata la probabilità, quello che minimizza il tempo è quello con l'indice più piccolo*/
        Task element_to_assign = (*buffer)[0];
        int index = -1;
        for (int i = 0; i < (*employees).size(); i++)
        {
            if ((*employees)[i].qual == element_to_assign.requested_qual && (*employees)[i].current_task.phase == 0)
            {
                if (DEBUG)
                    cout << "Assegnato al dip. " << i << " il task (" << (*buffer)[0].project.id << "," << (*buffer)[0].phase << "," << (*buffer)[0].requested_qual << ")\n";
                (*employees)[i].current_task = element_to_assign;
                buffer->erase(buffer->begin());
                return;
            }
        }
    }

public:
    void time_step(vector<Task> *buffer, vector<Employee> *employees, int ex3 = 0, int min_wait_time = 0)
    {
        time++;
        if ((*buffer).size() == 0)
        {
            return;
        }
        if (min_wait_time)
        {

            assign_task_minimizing_wait_time(buffer, employees);
        }
        else
        {

            assign_task(buffer, employees, ex3);
        }
    }
};
#endif