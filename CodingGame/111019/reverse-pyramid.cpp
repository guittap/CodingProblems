#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

int main()
{
    int N;
    cin >> N; cin.ignore();

    for(int i = N; i > 0; i--){
        for(int j = 0; j < i; j++){
            cout << N;
        }
        cout << endl;
    }
}