

#ifndef remanence_test_h
#define remanence_test_h

/* Macro to cause program to crash and core dump */
#define REMANENCE_CRASH { int * temp_ptr = 0; int i; i = *temp_ptr; }

// TODO define macros and the sensitive strings here - do not use static declarations here as it will show up in the core dump

#endif /* remanence_test_h */

