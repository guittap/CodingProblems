#include <iostream>
#include <fstream>

using namespace std;

int main() {
    ifstream inFile;
    inFile.open("/Users/wargen/Desktop/github/ICPCtraining/C++/spINPUT.txt");

    int x = 0;
    while (inFile >> x) {
        cout << x << endl;
    }

    inFile.close();
    return 0;
}