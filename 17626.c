#include <stdio.h>
#include <math.h>

long long *dparr;

long long dp(int depth) {
    if (dparr[depth] != 0) { return dparr[depth]; }
    dparr[depth] = dp(depth-1) + dp(depth-2);
    return dparr[depth]%10007; // 오버플로우가 발생하기 때문에 중간에 10007로 나눈 나머지 값을 사용하게 됨
}

int minus(int n) {
    return 0;
}

int main() {

    // dparr = (long long *) calloc(50001, sizeof(long long));
    // dparr[1] = 1; dparr[2] = 2; dparr[3] = 3;

    int n;
    int k;
    int c = 0;
    scanf("%d", &n);

    // printf("%d\n", (int)sqrt(n));

    while ( n != 0 ) {
        if (n < 0) { break; }

        k = (int)sqrt(n);
        printf("%d\n", k);
        n -= pow(k, 2); c++;
    }
    printf("\n%d", c);

    return 0;
}

// 사용자에게 받은 값으로 먼저 루트값을 구함. 그 루트값을 제곱해서 빼고 다시 dp를 구함. 이때 횟구를 구하는 거기 때문에 dp에는 