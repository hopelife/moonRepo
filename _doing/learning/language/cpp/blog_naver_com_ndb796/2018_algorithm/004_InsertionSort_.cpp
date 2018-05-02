#include <stdio.h>

int main(void) {
	int i, j, temp;
	int array[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
	for (i = 1; i < 10; i++) {
		temp = array[i];
		j = i;
		while (array[j-1] > temp && j > 0) {
			array[j] = array[j-1];
			j--;
		}
		array[j] = temp;

		for(int k = 0; k < 10; k++) {
			printf("%d ", array[k]);
		}

		printf("\n");
	}
	for(i = 0; i < 10; i++) {
		printf("%d ", array[i]);
	}
	return 0;
}
