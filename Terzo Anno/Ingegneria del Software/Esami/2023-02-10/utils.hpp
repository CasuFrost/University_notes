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
