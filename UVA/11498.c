#include <stdio.h>

int main(){
    int K,N,M,X,Y;
    scanf("%i",&K);
    while(K>0){
        scanf("%i %i",&N,&M);
        while(K>0){
            K--;
            scanf("%i %i",&X,&Y);
            if(X == N || M == Y){
                printf("divisa");
            }
            else if(X>N){
                if(Y>M){
                    printf("NE");
                }
                else{
                    printf("SE");
                }
            }
            else{
                if(Y>M){
                    printf("NO");
                }
                else{
                    printf("SO");
                }
            }
            printf("\n");
        }
        scanf("%i",&K);
    }
}