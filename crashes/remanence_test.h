

#ifndef remanence_test_h
#define remanence_test_h

/* Macro to cause program to crash and core dump */
#define REMANENCE_CRASH { int * temp_ptr = 0; int i; i = *temp_ptr; }

#endif /* remanence_test_h */

