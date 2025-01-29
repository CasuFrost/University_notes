#include "utils.hpp"
#include "employee.hpp"
#include "task.hpp"
#include "project_manager.hpp"
#include "task_gen.hpp"
#define precision_step 1000
void ex1(string file = "outputs.txt", int ex3 = 0, int min_wait_time = 0)
{
    vector<double> compl_time;
    int count = 0;
    double avg = 0;
    for (int k = 0; k < precision_step; k++)
    {
        vector<Employee> employees;
        int employees_counter = 0;
        for (int i = 0; i < Q; i++) // le qualifiche vanno da 1 a Q
        {
            for (int j = 0; j < W; j++)
            {
                Employee e(i + 1, employees_counter);
                employees.push_back(e);
                employees_counter++;
            }
        }
        vector<Task> buffer;
        TaskGenerator taskGenerator;
        DeliveryManager deliveryManager;
        ProjectManager projectManager;

        for (int l = 0; l < 10000; l++)
        {

            /*Task generator genera un task*/
            if (taskGenerator.time_step(&buffer))
            {
                break;
            }

            if (DEBUG)
            {
                cout << "Task buffer : \n";
                for (int i = 0; i < buffer.size(); ++i)
                {
                    cout << "(" << buffer[i].project.id << "," << buffer[i].phase << "," << buffer[i].requested_qual << ")  ";
                }
                cout << "\n";
            }

            /*Project manager lo assegna*/
            projectManager.time_step(&buffer, &employees, ex3, min_wait_time);

            if (DEBUG)
            {
                cout << "Dipendenti : \n";
                for (int i = 0; i < employees_counter; i++)
                {
                    cout << "     Employee " << i << " Qual : " << employees[i].qual;
                    if (employees[i].current_task.phase != 0)
                    {
                        cout << " Task : " << "(" << employees[i].current_task.project.id << "," << employees[i].current_task.phase << "," << employees[i].current_task.requested_qual << ")";
                    }
                    cout << "\n";
                }
                cout << "\n\n";

                usleep(DEBUG_TIME);
            }

            /*Employee lavorano*/
            for (int i = 0; i < employees_counter; i++)
            {

                employees[i].time_step(&deliveryManager);
            }
        }
        if (DEBUG)
        {
            cout << "progetti completati : \n";
            for (int i = 0; i < deliveryManager.finished_project.size(); i++)
            {
                cout << "      progetto : " << deliveryManager.finished_project[i].id << " nell'intervallo [" << deliveryManager.finished_project[i].start << "," << deliveryManager.finished_project[i].end << "]\n";
            }
        }

        if (deliveryManager.avg_completation_time() != -1)
        {
            avg += deliveryManager.avg_completation_time();
            compl_time.push_back(deliveryManager.avg_completation_time());
            count++;
            // cout << deliveryManager.avg_completation_time() << "\n";
        }
    }
    ofstream myFile(file);

    myFile << "ID = 2046212, MyMagicNumber = " << 1 + 2046212 % 173 << ", time = " << getCurrentTimeString()
           << "\n";
    myFile << "V =  " << avg_buffer(compl_time) << ", ";
    // cout << "VAR: " << (int)var_buffer(compl_time) << "\n";
    myFile << "S =  " << stdev_buffer(compl_time);
    myFile.close();
}

void ex2(string file = "outputs.txt", int ex3 = 0)
{
    ofstream myFile(file);
    vector<vector<double>> perc_time_dip;
    vector<double> compl_time;
    int count = 0;
    double avg = 0;
    for (int k = 0; k < precision_step; k++)
    {
        vector<Employee> employees;
        int employees_counter = 0;
        for (int i = 0; i < Q; i++) // le qualifiche vanno da 1 a Q
        {
            for (int j = 0; j < W; j++)
            {
                Employee e(i + 1, employees_counter);
                employees.push_back(e);
                employees_counter++;
                vector<double> tmp;
                perc_time_dip.push_back(tmp);
            }
        }
        vector<Task> buffer;
        TaskGenerator taskGenerator;
        DeliveryManager deliveryManager;
        ProjectManager projectManager;

        for (int l = 0; l < 10000; l++)
        {
            /*Task generator genera un task*/
            if (taskGenerator.time_step(&buffer))
                break;

            if (DEBUG)
            {
                cout << "Task buffer : \n";
                for (int i = 0; i < buffer.size(); ++i)
                {
                    cout << "(" << buffer[i].project.id << "," << buffer[i].phase << "," << buffer[i].requested_qual << ")  ";
                }
                cout << "\n";
            }

            /*Project manager lo assegna*/
            projectManager.time_step(&buffer, &employees, ex3);

            if (DEBUG)
            {
                cout << "Dipendenti : \n";
                for (int i = 0; i < employees_counter; i++)
                {
                    cout << "     Employee " << i << " Qual : " << employees[i].qual;
                    if (employees[i].current_task.phase != 0)
                    {
                        cout << " Task : " << "(" << employees[i].current_task.project.id << "," << employees[i].current_task.phase << "," << employees[i].current_task.requested_qual << ")";
                    }
                    cout << "\n";
                    // employees[i].time_step(deliveryManager);
                }
                cout << "\n\n";

                usleep(DEBUG_TIME);
                system("clear");
            }

            /*Employee lavorano*/
            for (int i = 0; i < employees_counter; i++)
            {
                employees[i].time_step(&deliveryManager);
            }
        }
        for (int i = 0; i < employees_counter; i++)
        {
            perc_time_dip[i].push_back(employees[i].working_time_perc());
        }
    }
    myFile << "ID = 2046212, MyMagicNumber = " << 1 + 2046212 % 173 << ", time = " << getCurrentTimeString() << "\n";
    int employees_counter = 0;
    for (int i = 0; i < Q; i++) // le qualifiche vanno da 1 a Q
    {
        for (int j = 0; j < W; j++)
        {
            myFile << "i = " << employees_counter << ", q =  " << Q << ", b = " << avg_buffer(perc_time_dip[employees_counter]) << ", s = " << stdev_buffer(perc_time_dip[employees_counter]) << "\n";
            employees_counter++;
        }
    }

    myFile.close();
}

int main(int argc, char **argv)
{
    setvbuf(stdout, NULL, _IONBF, 0);
    srand((unsigned)time(NULL));
    ex1("output/outputs1.txt");

    ex2("output/outputs2.txt");
    ex1("output/outputs3.txt", 1);

    ex2("output/outputs4.txt", 1);
    ex1("output/outputs5.txt", 1, 1);
}