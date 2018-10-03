
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
