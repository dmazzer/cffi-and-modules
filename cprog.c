#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "cprog.h"

int global_variable = 0;
int *globalptr;
int *globalptr2;

void setvar(int v)
{
    global_variable = v;
}

int getvar()
{
    return(global_variable);
}

void meminit(int v)
{
    globalptr = malloc(10*sizeof(int));
    for(int i=0; i<10; i++)
        globalptr[i] = v;
}

int memget(void)
{
    return globalptr[0];
}

void setvs(vs * vs_struct, int value )
{
    vs_struct->v1 = value;
}

int getvs(vs *vs_struct)
{
    return(vs_struct->v1);
}

int * new_meminit(int v)
{
    int *localptr;
    localptr = malloc(10*sizeof(int));
    for(int i=0; i<10; i++)
        localptr[i] = v;
    return(localptr);
}


void external_initmem(int* localptr)
{
    globalptr2 = localptr;
}

int getptr2(void)
{
    return globalptr2[0];
}

int main (void)
{

}