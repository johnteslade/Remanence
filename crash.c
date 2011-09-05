#include <stdlib.h>
#include <stdio.h>


void main(void)
{

	int * temp_ptr = 0;
	int i;
	
	char array[] = { 0xaa, 0xaa, 0xaa, 0xaa, 0xbb, 0xbb, 0xbb, 0xbb };

	char * malloc_array = NULL;

	malloc_array = malloc(5);

	malloc_array[0] = 0x11;
	malloc_array[1] = 0x11;
	malloc_array[2] = 0x22;
	malloc_array[3] = 0x22;

	i = *temp_ptr;

}

