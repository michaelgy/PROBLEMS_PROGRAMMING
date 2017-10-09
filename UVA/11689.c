#include <stdio.h>
#include <stdlib.h>

int main(){
    unsigned int N,e,f,c,acumulate;
    div_t division;
    scanf("%i",&N);
    for(;N>0;N--){
        scanf("%i %i %i",&e,&f,&c);
        acumulate = 0;
        division = div(e+f,c);
        while(division.quot+division.rem >= c){

            acumulate += division.quot;
            division = div(division.quot+division.rem,c);
        }
        acumulate += division.quot;
        printf("%i\n",acumulate);
    }
    return 0;
}
