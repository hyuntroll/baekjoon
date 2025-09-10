#include <stdio.h>

int n, m; // n은 1부터 n까지
int combi[8];

void nAndm(int start, int depth) {
    if ( depth == m ) { 
        for (int i=0; i<depth; ++i) {
            printf("%d ", combi[i]);
        }
        printf("\n"); return;
    }

    for (int i=start; i<=n; ++i) {
        combi[depth] = i;
        nAndm(i, depth+1);
    }
}

int main() {
    scanf("%d %d", &n, &m);

    nAndm(1, 0);

    return 0;
}