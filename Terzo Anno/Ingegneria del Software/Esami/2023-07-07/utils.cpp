#include <iostream>
#include <vector>
#include <random>
#include <time.h>
#include <cstring>
#include <numeric>
#include <cmath>
#include <string>
#include <sstream>
#include <fstream>
#include <bits/stdc++.h>
using namespace std;

#ifndef UTILS_HPP
#define UTILS_HPP

#define DEBUG 0

/*Parametri dell'esame*/
#define L 10
#define D 1
#define B 20
#define N 10
#define W 5
#define Q 3

/*Fine parametri dell'esame*/

vector<string>
splitString(const string &str)
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

double rand_float_0_1()
{
    return ((double)rand() / (double)RAND_MAX);
}

int randi_range(int a, int b)
{
    return a + rand() % (b - a + 1);
}

double max_buffer(vector<double> buffer)
{
    double max = buffer[0];
    for (int i = 0; i < buffer.size(); i++)
    {
        if (buffer[i] > buffer[0])
        {
            max = buffer[i];
        }
    }
    return max;
}

double max_buffer(vector<int> buffer)
{
    int max = buffer[0];
    for (int i = 0; i < buffer.size(); i++)
    {
        if (buffer[i] > max)
        {
            max = buffer[i];
        }
    }
    return max;
}

double avg_buffer(vector<double> buffer)
{
    if (buffer.size() == 0)
    {
        return 0;
    }
    double sum = 0.;
    for (int i = 0; i < buffer.size(); i++)
    {
        sum += buffer[i];
    }

    return sum / (double)buffer.size();
}

double avg_buffer(vector<int> buffer)
{
    double sum = 0.;
    for (int i = 0; i < buffer.size(); i++)
    {
        sum += buffer[i];
    }

    return sum / (double)buffer.size();
}

double var_buffer(vector<double> buffer)
{
    double varianza = 0.0;
    double avg = avg_buffer(buffer);
    for (double numero : buffer)
    {
        varianza += pow(numero - avg, 2);
    }

    varianza /= (double)buffer.size();
    return varianza;
}

double var_buffer(vector<int> buffer)
{
    double varianza = 0.0;
    double avg = avg_buffer(buffer);
    for (int numero : buffer)
    {
        varianza += pow(numero - avg, 2);
    }

    varianza /= (double)buffer.size();
    return varianza;
}

double stdev_buffer(vector<int> buffer)
{
    return (int)sqrt(var_buffer(buffer));
}

double stdev_buffer(vector<double> buffer)
{
    return (double)sqrt(var_buffer(buffer));
}

string getCurrentTimeString()
{
    // Get current time point
    auto now = chrono::system_clock::now();

    // Convert to time_t for use with localtime
    time_t currentTime = chrono::system_clock::to_time_t(now);

    // Convert to local time
    tm *localTime = localtime(&currentTime);

    // Create a stringstream to format the time
    stringstream ss;

    // Format the time as you desire (example: HH:MM:SS)
    ss << put_time(localTime, "%H:%M:%S");

    return ss.str();
}

#endif