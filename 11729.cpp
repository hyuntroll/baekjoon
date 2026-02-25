#include <iostream>
#include <cmath>
using namespace std;

void hanoi(int n, int start, int step, int end) {
    if (n == 1) {
        cout << start << " " << end << "\n";
    }
    else {
        hanoi(n-1, start, end, step);
        cout << start << " " << end << "\n";
        hanoi(n-1, step, start, end);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int num;
    cin >> num;

    long long res = (long long)pow(2, num) - 1;
    cout << res << "\n";
    if (num <= 20) {
        hanoi(num, 1, 2, 3);
    }
    

    return 0;
}