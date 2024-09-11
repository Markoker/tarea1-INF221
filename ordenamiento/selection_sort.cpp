#include <bits/stdc++.h>
#include <chrono>
using namespace std;


// Function for Selection sort
void selectionSort(vector<int> arr, int n)
{
    // One by one move boundary of
    // unsorted subarray
    for (int i = 0; i < n - 1; i++)
    {
        // Find the minimum element in
        // unsorted array
        int min_idx = i;
        for (int j = i + 1; j < n; j++)
        {
            if (arr[j] < arr[min_idx])
                min_idx = j;
        }

        // Swap the found minimum element
        // with the first element
        if (min_idx != i)
            swap(arr[min_idx], arr[i]);
    }
}

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
        selectionSort(arr, arr.size());
        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
        cout << arr.size() << "," << duration.count() << endl;

    }

    return 0;
}
