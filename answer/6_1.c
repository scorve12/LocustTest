#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int cnt, count = 1;
	int arr[4][4];
	int n, r, c, res = 0;

	for (int i = 1; i < 4; i++) {
		scanf("%d %d %d", &arr[i][1], &arr[i][2], &arr[i][3]);
	}
	scanf("%d", &n);

	for (int k = 0; k < n; k++) {
		cnt = 0;

		scanf("%d %d", &r, &c);
		if (arr[r][c] == 0)
			arr[r][c] = 1;
		else
			arr[r][c] = 0;

		if (r == 2 || r == 3)
			if (arr[r - 1][c] == 0)
				arr[r - 1][c] = 1;
			else
				arr[r - 1][c] = 0;

		if (r == 1 || r == 2)
			if (arr[r + 1][c] == 0)
				arr[r + 1][c] = 1;
			else
				arr[r + 1][c] = 0;

		if (c == 2 || c == 3)
			if (arr[r][c - 1] == 0)
				arr[r][c - 1] = 1;
			else
				arr[r][c - 1] = 0;
		if (c == 1 || c == 2)
			if (arr[r][c + 1] == 0)
				arr[r][c + 1] = 1;
			else
				arr[r][c + 1] = 0;

		cnt = 0;
		for (int i = 1; i < 4; i++) {
			if (arr[i][1] == arr[i][2] && arr[i][2] == arr[i][3])
				cnt++;
		}

		if (cnt == 3 && arr[1][1] == arr[2][1] && arr[2][1] == arr[3][1])
			res = count;
		if (res == 0)
			count++;
	}
	if (res == 0)
		printf("-1");
	else
		printf("%d", res);
	return 0;
}