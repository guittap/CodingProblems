#include <iostream> 

using namespace std;

int main() {
    int stars = 0;
    while (cin >> stars) {
        cout << stars << ":" << endl;
        for (int i = 2; i <= (stars/2)+1; i++) {
            for (int j = i-1; j <= i; j++) {
                if (stars % (i + j) == 0 || stars % (i + j) == i) {
                    cout << " " << i << "," << j << endl;
                }
            }
        }
    }

    return 0;
}