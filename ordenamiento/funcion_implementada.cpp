#include <bits/stdc++.h>
#include <chrono>
using namespace std;


int main(int argc, char const *argv[])
{
    if (argc < 2)
    {
        cout << argv[0] << " requires an array" << endl;
    }
    cout << "Tamaño,Tiempo" << endl;
    std::ifstream infile(argv[1]);
    std::string line;

    while (std::getline(infile, line)) {
        std::stringstream ss(line);
        std::vector<int> arr;
        int num;
        while (ss >> num) {
            arr.push_back(num);
            if (ss.peek() == ',') {
                ss.ignore();
            }
        }


        auto start = chrono::high_resolution_clock::now();


        sort(arr.begin(), arr.end());


        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
        cout << arr.size() << "," << duration.count() << endl;
    }

    return 0;
}