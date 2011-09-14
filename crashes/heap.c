#include <stdlib.h>
#include <stdio.h>

#include "remanence_test.h"

/*
 *
 * Remanence Test
 *
 * Bytes on the heap
 *
 */

void main(void)
{

	char * malloc_array = NULL;

	malloc_array = malloc(5);

	malloc_array[0] = 0x11;
	malloc_array[1] = 0x11;
	malloc_array[2] = 0x22;
	malloc_array[3] = 0x22;

	REMANENCE_CRASH

}

