#include "dtmc.cpp"
using namespace std;

class Customer
{

private:
    double avg;
    double stdDev;
    int waiting_time_steps = 0;
    void read_from_file(string filename, int skip = 0)
    {
        int num_state;
        ifstream file(filename);
        string line;
        getline(file, line);
        if (skip)
            getline(file, line);
        vector<string> words = splitString(line);
        if (words.size() == 0)
        {
            cout << "ERROR in file : " << filename << "\n";
            return;
        }
        if (words[0] == "Avg")
        {
            avg = stoi(words[1]);
        }
        else
        {
            cout << "ERROR, file " << filename << " have wrong format\n";
            return;
        }
        getline(file, line);
        words = splitString(line);
        if (words[0] == "StdDev")
        {
            stdDev = stoi(words[1]);
        }
        else
        {
            cout << "ERROR, file " << filename << " have wrong format\n";
            return;
        }
    }

public:
    Customer(string filename, int skip = 0)
    {
        read_from_file(filename, skip);
    }
    Customer(double avg, double stdDev)
    {
        this->avg = avg;
        this->stdDev = stdDev;
        random_device rd;
        mt19937 gen(rd());
        normal_distribution<double> dis(avg, stdDev);
        waiting_time_steps = (int)dis(gen);
    }

    /*Simula uno step di tempo, torna 1 se la richiesta avviene, altrimenti 0*/
    int simulate_step()
    {
        random_device rd;
        mt19937 gen(rd());
        normal_distribution<double> dis(avg, stdDev);
        if (waiting_time_steps == 0)
        {
            /*Invia richiesta e re-setta il tempo di attesa*/
            waiting_time_steps = (int)dis(gen);
            return 1;
        }
        else
        {
            waiting_time_steps--;
        }
        return 0;
    }
};