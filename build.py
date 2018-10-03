from cffi import FFI
import os
ffibuilder = FFI()

PATH = os.path.dirname(__file__)


ffibuilder.cdef("""

typedef struct {
    int v1;
    int v2;
} vs;

void setvar(int v);
int getvar(void);
void meminit(int v);
int memget(void);
int * new_meminit(int v);
void setvs(vs * vs_struct, int value );
int getvs(vs *vs_struct);

""")

ffibuilder.set_source("_cprog",
"""
     #include "cprog.h"   // the C header of the library
""",
     libraries=['m', ],
     sources=['cprog.c'])   # library name, for the linker


if __name__ == "__main__":
    ffibuilder.compile(verbose=True)