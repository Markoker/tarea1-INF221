#include <bits/stdc++.h>
#include <chrono>
using namespace std;


// Merges two subarrays of arr[].
// First subarray is arr[left..mid]
// Second subarray is arr[mid+1..right]
void merge(vector<int>& arr, int left, int mid, int right)
{
    int n1 = mid - left + 1;
    int n2 = right - mid;

    // Create temp vectors
    vector<int> L(n1), R(n2);

    // Copy data to temp vectors L[] and R[]
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    int i = 0, j = 0;
    int k = left;

    // Merge the temp vectors back
    // into arr[left..right]
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }

    // Copy the remaining elements of L[],
    // if there are any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }

    // Copy the remaining elements of R[],
    // if there are any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}


void mergeSort(vector<int>& arr, int left, int right)
{
    if (left >= right)
        return;

    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
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


        mergeSort(arr, 0, arr.size() - 1);


        auto end = chrono::high_resolution_clock::now();
        auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);
        cout << arr.size() << "," << duration.count() << endl;
    }

    return 0;
}
