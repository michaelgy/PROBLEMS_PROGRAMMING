#include <cstdio>
#include <cmath>

using namespace std;


int main(){
    int n,suma,i;
    printf("PERFECTION OUTPUT\n");
    for(scanf("%d",&n);n!=0; scanf("%d",&n)){
        suma = 1;
        for(i=2; i<n/2+1 && suma<n;i++){
            if(n%i== 0){
                suma+=i;
            }
        }
        suma = n==1?0:suma;
        printf("%5d  ",n);
        if(suma == n){
            printf("PERFECT\n");
        }
        else if(suma<n){
            printf("DEFICIENT\n");
        }
        else{
            printf("ABUNDANT\n");
        }
    }
    printf("END OF OUTPUT\n");
    return 0;
}