#include <bits/stdc++.h>
#include <chrono>
using namespace std;
typedef long long lld;


lld** multiplicacionSimple(lld** a, lld** b, int n, int l, int m)
{
	lld** c = new lld*[n];
	for (int i = 0; i < n; i++)
		c[i] = new lld[m];

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			c[i][j] = 0;
			for (int k = 0; k < l; k++) {
				c[i][j] += a[i][k] * b[k][j];
			}
		}
	}
	return c;
}


int main(int argc, char const *argv[])
{
    if (argc < 2)
    {
        cout << argv[0] << " requires an array" << endl;
    }
    cout << "n1,n2,n3,n4,Tiempo" << endl;
    std::ifstream infile(argv[1]);
    std::string line;

	int n1, n2, n3, n4;

    while (std::getline(infile, line)) {
        std::stringstream ss(line);
        int num;

		ss >> n1;
		ss >> n2;
		ss >> n3;
		ss >> n4;

		lld** a = new lld*[n1];
		for (int i = 0; i < n1; i++) {
            a[i] = new lld[n2];
			std::getline(infile, line);
        	std::stringstream ss(line);

            for (int j = 0; j < n2; j++) {
                ss >> num;
                a[i][j] = num;
            }
        }

	    lld** b = new lld*[n3];
		for (int i = 0; i < n3; i++) {
        	b[i] = new lld[n4];

			std::getline(infile, line);
        	std::stringstream ss(line);
        	for (int j = 0; j < n4; j++) {
            	ss >> num;
           		b[i][j] = num;
        	}
		}

		auto start = chrono::high_resolution_clock::now();
		lld** c = multiplicacionSimple(a, b, n1, n2, n4);
    	auto end = chrono::high_resolution_clock::now();

    	auto duration = chrono::duration_cast<chrono::nanoseconds>(end - start);

    	cout << n1 << "," << n2 << "," << n3 << "," << n4 << "," << duration.count() << endl;

		for (int i = 0; i < n1; i++) delete[] a[i];
		delete[] a;

		for (int i = 0; i < n3; i++) delete[] b[i];
		delete[] b;

		for (int i = 0; i < n1; i++) delete[] c[i];
		delete[] c;
	}

    return 0;
}
