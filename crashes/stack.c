#include <stdlib.h>
#include <stdio.h>

#include "remanence_test.h"

/*
 *
 * Remancence Test
 *
 * Bytes on the stack.  This is partially copied into 
 * another stack variable
 *
 */

void main(void)
{
	
	char array[] = { 0xaa, 0xaa, 0xaa, 0xaa, 0xbb, 0xbb, 0xbb, 0xbb };

	char array2[10] = {0};

	memcpy(array2 + 2, array + 3, 4);

	REMANENCE_CRASH

}

