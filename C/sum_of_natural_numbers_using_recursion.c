#include <stdio.h>

int sum(int n) {
	if (n != 0)
		// sum() function calls itself
		return n + sum(n - 1);
	else
		return n;
}

int main() {
	int number, result;

	printf("Enter a positive integer: ");
	scanf("%d", &number);

	result = sum(number);

	printf("Sum = %d\n", result);
	return 0;
}
