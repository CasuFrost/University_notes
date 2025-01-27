#include "worker.hpp"

class ProjectManager
{
public:
    ProjectManager()
    {
    }

    void time_step(vector<vector<Worker>> *worker, vector<Task> *taskBuffer)
    {
        if ((*taskBuffer).size() == 0)
        {
            return;
        }

        Task to_rm = (*taskBuffer).at(0);

        for (int i = 0; i < (*worker)[0].size(); i++)
        {
            if ((*worker)[to_rm.q][i].state == 0)
            {
                (*worker)[to_rm.q][i].currTask = to_rm;
                (*worker)[to_rm.q][i].state = to_rm.k;
                (*taskBuffer).erase((*taskBuffer).begin());
                // if(DEBUG) cout << "il PM assegna al worker " << "" << " il task" << "(" << to_rm.v << ", " << to_rm.k << ", " << to_rm.q << ")\n";
                return;
            }
        }
    }
};
