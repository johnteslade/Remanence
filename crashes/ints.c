#include <stdlib.h>
#include <stdio.h>

#include "remanence_test.h"

/*
 *
 * Remanence Test
 *
 * Data stored within ints
 *
 */

void main(void)
{

	char array[] = { 0xaa, 0xaa, 0xaa, 0xaa, 0xbb, 0xbb, 0xbb, 0xbb 0xcc, 0xcc, 0xcc, 0xcc};
 

	int a = 0;
	
	// Copy in the data
	memcpy(&a, array + 2, sizeof(int));
	
	//TODO do an endian test here.  Need to manually set it into the integer based on known endianness.

	/* Sanitise static array so we don't get false positives */
	memset(array, 0x00, sizeof(array));

	REMANENCE_CRASH

}

