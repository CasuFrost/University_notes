#include "utils.hpp"
#include "task.hpp"
#ifndef DEL_MAN_HPP
#define DEL_MAN_HPP
class DeliveryManager
{

public:
    vector<Project> finished_project;
    void add_project(Project proj)
    {
        finished_project.push_back(proj);
    }

    double avg_completation_time()
    {
        if (finished_project.size() == 0)
        {
            return -1;
        }
        double sum = 0.;
        for (int i = 0; i < finished_project.size(); i++)
        {
            sum += (double)finished_project[i].end - (double)finished_project[i].start;
        }
        return sum / (double)finished_project.size();
    }

    double var_completation_time()
    {
        double varianza = 0.0;
        double avg = avg_completation_time();
        for (int i = 0; i < finished_project.size(); i++)
        {
            varianza += pow((double)finished_project[i].end - (double)finished_project[i].start - avg, 2);
        }
        varianza /= finished_project.size();
        return varianza;
    }

    double stdev_completation_time()
    {
        return sqrt(var_completation_time());
    }
};
#endif