#include <stdio.h>
#include <stdlib.h>

long long *dparr;

long long dp(int depth) {
    if (dparr[depth] != 0) { return dparr[depth]; }
    dparr[depth] = dp(depth-1) + dp(depth-2);
    return dparr[depth]%10007; // 오버플로우가 발생하기 때문에 중간에 10007로 나눈 나머지 값을 사용하게 됨
}

int main() {

    dparr = (long long *) calloc(1001, sizeof(long long));
    dparr[1] = 1; dparr[2] = 2;

    int n;
    scanf("%d", &n);
    printf("%lld", dp(n));

    return 0;
}