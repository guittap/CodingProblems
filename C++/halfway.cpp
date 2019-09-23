#include <iostream>
#include <math.h>

using namespace std;

int main() {
    int n = 0;
    while (cin >> n) {
        cout << ceil((-sqrt(2) * sqrt((n*n) - (2*n) + 1) + (2*n) - 2) / 2) << endl;
    }
    return 0;
}