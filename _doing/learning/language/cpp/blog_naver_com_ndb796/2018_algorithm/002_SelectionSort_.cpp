#include <stdio.h>

int main(void) {
	int i, j, max, index, temp;
	int array[10] = {1, 10, 5, 8, 7, 6, 4, 3, 2, 9};
	for(i = 9; i > 0; i--) {
		max = -9999;
		for(j = 0; j < i+1; j++) {
			if(max < array[j]) {
				max = array[j];
				index = j;
			}
		}
		temp = array[i];
		array[i] = array[index];
		array[index] = temp;

		printf("i: %d [", i);
		for(int k = 0; k < 10; k++) {
			printf("%d ", array[k]);
		}

		printf("]\n");
	}

	for(i = 0; i < 10; i++) {
		printf("%d ", array[i]);
	}

	return 0;
}
