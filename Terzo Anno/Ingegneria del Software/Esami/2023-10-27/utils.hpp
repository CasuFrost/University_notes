#include <iostream>
#include <vector>
#include <random>
#include <time.h>
#include <cmath>
#define DEBUG 0

using namespace std;

vector<string> splitString(const string &str)
{
    vector<string> words;
    string word;

    for (char c : str)
    {
        if (isspace(c))
        {
            if (!word.empty())
            {
                words.push_back(word);
                word.clear();
            }
        }
        else
        {
            word += c;
        }
    }

    // Aggiungi l'ultima parola se non è vuota
    if (!word.empty())
    {
        words.push_back(word);
    }

    return words;
}

class DeliveryManager
{
private:
    vector<int> deliveryTimes;
    vector<int> projectBuffer;

public:
    DeliveryManager() {}
    vector<pair<int, int>> project_and_starting_times;
    void project_complete(int v)
    {
        projectBuffer.push_back(v);
    }
    void new_project(int a, int b)
    {
        project_and_starting_times.push_back({a, b});
        // project_and_starting_times.push_back(t);
    }
    void print_project()
    {
        for (const auto &pair : project_and_starting_times)
        {
            cout << "First: " << pair.first << ", Second: " << pair.second << "\n";
        }
    }
};