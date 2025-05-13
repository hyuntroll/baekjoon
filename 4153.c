#include <stdio.h>
#include <math.h>
#define max(x, y) (x) > (y) ? (x) : (y) 

int main() {
	for (;;) {
		int a, b, c, max_;

		scanf_s("%d %d %d", &a, &b, &c);
		//printf("%d %d %d", a, b, c);

		if (a == 0 && b == 0 && c == 0) {
			break;
		}

		max_ = max(max(a, b), max(b, c));

		if (pow(a, 2) + pow(b, 2) + pow(c, 2) == 2 * pow(max_, 2)) {
			printf("right\n");
		}
		else {
			printf("wrong\n");
		}
		

	}

	return 0;
}