#include <stdio.h>

int main(){
    int t,a,b,c,i;
    scanf("%i",&t);
    for(i=0;t>i;i++){
        scanf("%i %i %i",&a,&b,&c);
        printf("Case %i: %d\n",i+1, a>b? ( a>c? ( b>c ?b:c):a ) : ( b>c ? (a>c?a:c) : b) );
    }
}