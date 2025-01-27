
#include "dispatcher.hpp"
using namespace std;
int main(int argc, char **argv)
{
    srand((unsigned)time(NULL));
    setvbuf(stdout, NULL, _IONBF, 0);
    DTMC m_chain("parameters.txt");
    cout << m_chain.expected_cost_mc_simulation(1000, 2);
    return 0;
    // DTMC m_chain(state, edge_prob, edge_cost);
    // m_chain.print_mc();
    // double expected = m_chain.expected_cost_mc_simulation(10000, 0);
    // cout << "expected cost : " << expected << "\n";
    // cout << "Prob(cost <= " << expected << ") = " << m_chain.probability_max_cost(10000, expected, 2) << "\n";
    //  cout << "expected cost : " << m_chain.expected_cost_mc_simulation(1000, 0) << "\n";
    // m_chain.print_mc();
    vector<Customer> C;
    for (int i = 0; i < 4; i++)
    {
        Customer tmp("parameters3.txt");
        C.push_back(tmp);
    }
    Dispatcher D(C.size());

    for (int i = 0; i < 30; i++)
    {
        vector<int> tmp;
        for (Customer &c : C)
        {
            tmp.push_back(c.simulate_step());
        }
        D.simulate_step(tmp, i);
    }
    // D.print_message_list();
    // cout << D.check_order_preservation() << "\n";
    // m_chain.printlog();
}