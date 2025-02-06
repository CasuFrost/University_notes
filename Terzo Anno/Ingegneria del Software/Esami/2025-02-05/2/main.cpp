#include "dtmc.cpp"
#include "drone.cpp"
int simulation()
{
    /*parametri*/
    double C;
    int H = 1000;
    int N = 4;
    double X1 = -5;
    double Y1 = -2;
    double X2 = 10;
    double Y2 = 7;
    int M = 3;

    /*Lettura dei parametri*/
    ifstream file("parameters.txt");
    string line;
    getline(file, line);
    vector<string> tmp = splitString(line);
    if (tmp[0] == "C")
        C = stof(tmp[1]);
    getline(file, line);
    if (tmp[0] == "H")
        H = stoi(tmp[1]);
    getline(file, line);
    tmp = splitString(line);
    if (tmp[0] == "N")
        N = stoi(tmp[1]);
    getline(file, line);
    tmp = splitString(line);
    X1 = stof(tmp[0]);
    X2 = stof(tmp[1]);
    Y1 = stof(tmp[2]);
    Y2 = stof(tmp[3]);
    getline(file, line);
    if (tmp[0] == "M")
        M = stoi(tmp[1]);
    vector<Area2D> M_points;
    while (getline(file, line))
    {
        tmp = splitString(line);
        M_points.push_back(Area2D(stof(tmp[0]), stof(tmp[1])));
    }
    file.close();
    // cout << X1 << " " << X2 << " " << Y1 << " " << Y2 << " " << N << " " << M << " " << H;

    /*creazione elementi*/
    vector<Drone> drones;
    for (int i = 0; i < N; i++) /*creazione di N droni*/
    {
        Drone d(X1, Y1, X2, Y2);
        drones.push_back(d);
    }

    /*per ogni punto da monitorare c'è un vettore che conta i droni in quel punto*/
    vector<vector<int>> monitor_points_vec;
    for (int i = 0; i < M; i++)
    {
        vector<int> v(H, 0);
        monitor_points_vec.push_back(v);
    }

    /*copertura*/
    vector<vector<double>> copertura;
    for (int i = 0; i < M; i++)
    {
        vector<double> v(H, 0.0);
        copertura.push_back(v);
    }

    for (int time = 0; time < H; time++) /*ciclo di simulazione*/
    {
        /*droni clacolano le posizioni*/
        for (int i = 0; i < N; i++)
        {
            drones[i].time_step();
            for (int j = 0; j < M; j++)
            {
                /*controllo area*/
                if (drones[i].x >= M_points[j].X - 1 && drones[i].x <= M_points[j].X + 1 &&
                    drones[i].y >= M_points[j].Y - 1 && drones[i].y <= M_points[j].Y + 1)
                {
                    /*Drone nel punto */
                    monitor_points_vec[j][time] += 1;
                    // cout<<"in area "<<
                }
            }
        }
        // cout << "\n";
    }

    /*calcolo copertura*/
    for (int m = 0; m < M; m++)
    {
        copertura[m][0] = (double)0;
    }
    for (int i = 1; i < H; i++)
    {
        for (int m = 0; m < M; m++)
        {
            copertura[m][i] = copertura[m][i - 1] * ((double)(i - 1) / (double)(i)) +
                              ((double)monitor_points_vec[m][i]) / ((double)i);
        }
    }

    for (int m = 0; m < M; m++)
    {
        if (copertura[m][H - 1] < C)
        {
            return 0;
        }
    }

    return 1;
}

int main(int argc, char **argv)
{
    srand((unsigned)time(NULL));
    setvbuf(stdout, NULL, _IONBF, 0);
    int steps = 1000;
    int num = 0;
    for (int i = 0; i < steps; i++)
    {
        num += simulation();
    }
    ofstream output("results.txt");
    output << "2025-02-05-marco-casu-2046212\n";

    output << "P " << (float)num / (float)steps;

    output.close();
    return 0;
}