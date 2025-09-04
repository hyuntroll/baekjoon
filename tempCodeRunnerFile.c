#include <stdio.h>
#include <stdlib.h>

long long * dparr;
// int타입 이슈;


long long dp(int depth) {
    if (! (1 <= depth && depth <= 10) ) {
        if (dparr[depth] != 0) { return dparr[depth];}
        dparr[depth] = dp(depth-1) + dp(depth-5);
    }

    return dparr[depth];
}

int main(void) {

    int n;
    int k;
    scanf("%d", &n); fflush(stdin);
    dparr = (long long *) calloc(n+1, sizeof(long long)); // n+1만큼 할당 후 0으로 초기화
    dparr[1] = 1; dparr[2] = 1; dparr[3] = 1; dparr[4] = 2; dparr[5] = 2; 
    dparr[6] = 3; dparr[7] = 4; dparr[8] = 5; dparr[9] = 7; dparr[10] = 9;
    for ( int i = 0 ; i<n; i++) {
        scanf("%d", &k); fflush(stdin);
        printf("%lld\n", dp(k));
    }
    free(dparr);

    return 0;
}

