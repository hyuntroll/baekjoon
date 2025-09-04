#include <stdio.h>
#include <stdlib.h>

int *dparr;

int dp(int n) {
    if (1 <= n && n <= 3) { return dparr[n]; }
    dparr[n] = dp(n-1) + dp(n-2) + dp(n-3);
    return dparr[n];
}

int main(void) {

    int n;
    int k;
    scanf("%d", &n);

    dparr = (int * ) malloc(sizeof(int) * 12);
    dparr[1] = 1; dparr[2] = 2; dparr[3] = 4;
    for (int i=0; i<n; i++) {
        scanf("%d", &k); fflush(stdin);
        printf("%d\n", dp(k));
    }

    free(dparr);

    return 0;
}