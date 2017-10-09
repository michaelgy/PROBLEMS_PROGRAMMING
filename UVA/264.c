#include <stdio.h>

int main(){
    int k,ak,akn,i,n;
    n = scanf("%d",&i);
    while(n!=EOF){
        printf("TERM %d IS ",i);
        ak = 0;
        akn = 1;
        k=1;
        while(i>akn){
            k++;
            ak = akn;
            akn = k*(k+1)/2;
        }
        if(i==1){
            printf("1/1");
        }
        else if(k%2==0){
            if(i==akn){
                printf("%d/1",k);
            }
            else{
                n = i-ak;
                printf("%d/%d",n,k-(n-1));
            }
        }
        else{
            if(i==akn){
                printf("1/%d",k);
            }
            else{
                n = i-ak;
                printf("%d/%d",k-(n-1),n);
            }
        }
        printf("\n");
        n = scanf("%d",&i);
    }
    return 0;
}