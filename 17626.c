#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// 구하려는 수의 뤁트값을 먼저 구함
// 그 루트값을 가지고 제곱근 반복돌림
// 금마 가지고 DP[n-k**2] 를 하면 n-k**2까지 했을 때 최소값을 가질 수 있고 그 다음에 k**2를 더하면 결과적으로 n을 구할 수 있으니 +1해줌 

int * dparr;

int dp(int n) {
    if (dparr[n] != 0) { return dparr[n]; }
    int kkk = (int) (sqrt(n));
    int temp;
    if ( n == kkk*kkk) {
        dparr[n] = 1;
        return 1;
    }
    int min = 1000000;
    for (int i = kkk; i > 0; i--) {
        temp = dp(n- i*i); 
        min = (min > temp+1) ? temp+1 : min;
    }
    dparr[n] = min;
    return min;

}

int main() {
    int n;
    dparr = (int *) calloc(50001, sizeof(int));
    dparr[1] = 1; dparr[2] = 2; dparr[3] = 3; dparr[4] = 1;
    scanf("%d", &n);
    printf("%d", dp(n));



    return 0;
}

