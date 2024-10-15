#pragma warning(disable: 4996)
#include<stdio.h>

int main(void)
{
	int q;
	int i = 0;
	int a = 1, b = 1;
	char str[200];

	scanf("%d", &q);

	scanf(" %[^\n]s", str);

	while (str[i] != '\0') {

		if (str[i] == 'R') {
			if (b + 1 <= q) b = b + 1;
			else b = q;
		}
		else if (str[i] == 'L') {
			if (b - 1 >= 1)	b = b - 1;
			else b = 1;
		}
		else if (str[i] == 'U') {
			if (a - 1 >= 1)	a = a - 1;
			else a = 1;
		}
		else if (str[i] == 'D') {
			if (a + 1 <= q)	a = a + 1;
			else a = q;
		}
		i++;
	}
	printf("%d %d", a, b);

	return 0;

}