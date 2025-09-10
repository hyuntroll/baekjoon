#include <stdio.h>
#include <stdlib.h>

int arr[21][21];
int team1[20] = {0};
int team2[20] = {0};
int visited[21] = {0};
int k, n, j;
int min_score = 201;
int score1, score2, total;


void backtracking(int start, int depth) {
    if (depth == k) {
        // team1에 있는 값 더하고, visited에 없는 값들 모아서 다시 구하기
        score1 = 0; score2 = 0; j = 0;

        for (int i=1; i<=n; ++i) {
            if (j >= k) { break; }
            if (!visited[i]) { team2[j++] = i; }
        }
        for (int i=0; i<k; i++) {
            for (int j=i+1; j<k; j++) {
                score1 += arr[team1[i]][team1[j]] + arr[team1[j]][team1[i]];
                score2 += arr[team2[i]][team2[j]] + arr[team2[j]][team2[i]];
            }
        }
        total = abs(score1-score2);
        min_score = (min_score > total) ? total : min_score;

        return;
    }
    for (int i=start; i<=n; i++) {
        // if (depth == 0 && i == k) { break; } // 맨 처음이랑 맨 마지막은 1 2    3 4로 사실상 같음
        team1[depth] = i;
        visited[i] = 1;
        backtracking(i+1, depth+1);
        visited[i] = 0;
    }

}


int main() {
 
    scanf("%d", &n);
    k = n/2;

    for (int i=1; i<=n; ++i) {
        for (int j=1; j<=n; ++j) {
         scanf("%d", &arr[i][j]);   
        }

    }

    // holyshit(0);
    backtracking(1, 0);
    printf("%d", min_score);

    return 0;
}



