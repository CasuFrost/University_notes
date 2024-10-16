using namespace std;
#include <iostream>
#include <vector>

int main()
{
    vector<int> a;
    vector<vector<int>> b;
    a.push_back(1);
    a.push_back(2);
    b.push_back(a);
    for (int k : a)
    {
        cout << k << "\n";
    }
}