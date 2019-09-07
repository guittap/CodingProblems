#include <iostream>
#include <cmath>

using namespace std;

#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

int main() {
    int nums[4] = { 1,4,2,3 };
    int max = abs(nums[0] - nums[1]);
    bool isJolly = true;
    for (int i = 1; i < (sizeof(nums) / sizeof(int)) - 1; i++) {
        if (max < abs(nums[i] - nums[i + 1])) {
            isJolly = false;
        }
        else {
            max = abs(nums[i] - nums[i + 1]);
        }
    }

    if (isJolly) {
        cout << "Jolly" << endl;
    }

    else {
        cout << "Not jolly" << endl;
    }

    return 0;
}