#include <stdio.h>

int main(){
    unsigned int a,b;
    int i;
    for(i=scanf("%d %d",&a,&b); i==2;i=scanf("%d %d",&a,&b)){
        printf("%d\n",a^b);
    }
    return 0;
}