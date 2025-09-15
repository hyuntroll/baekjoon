#include <stdio.h>

int n, m;
int visited[1001];
int arr[1001][1001];

void dfs(int i) {
    visited[i] = 1;
    for (int k=1; k<=n; k++) {
        if (arr[i][k] && !visited[k]) {
            dfs(k);
        }
    }

}

// 노드가 서로 이어져 있고, 탐색을 했는지 안했는지 알기 위해 visited를 나둠
// 어느 노드가 활성화 되어있는지 알기위해 arr[a][b] = 1 [b][a] = 1를 통해 b-a a-b 모두 연결되어있음을 명시해줌
// 안에 들어가 있는 a,b의 값은 1~n이기 때문에 for문으로 순차적으로 돌림.
// 순차적으로 dfs를 하면서 방문을 하면 visited를 하고 그게 아니라면 이와 연결되어있는 다른 노드를 찾기 위해 다시 순환함
// 이렇게 순환하면 dfs에서 만난 노드와 다른 노드가 연결되어있는지 아닌지 확인할 수 있고, 탐색은 연결된 노드끼리만 하게됨
// 탐색을 하면 연결되어있는 모든 노드는 visited가 1이고 연결되어 있으니 cnt++를 해준다
// 다시 탐색을 하는데 이미 방문했으면 무시하고, 하지 않았다면 윗 과정을 똑같이 반복한다

int main() {

    int a, b;
    int cnt = 0;
    scanf("%d %d", &n, &m);
    for (int i=0; i< m; i++) {
        scanf("%d %d", &a, &b);
        arr[a][b] = 1;
        arr[b][a] = 1;
    }
    for(int i=1; i<=n; i++) {
        if(!visited[i]) {
            dfs(i);
            cnt++;
        }
    }

    printf("%d\n", cnt);

    return 0;
}