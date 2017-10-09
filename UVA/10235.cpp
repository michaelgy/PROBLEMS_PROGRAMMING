#include <cmath>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cstdlib>

#define MAX 1e6
#define MAXP (int)sqrt(MAX)

using namespace std;

int main(){
    int numbers[(int)MAXP/2],primes[(int)(2*MAXP/log(MAXP))];
    int i,j,n,pcount,nc;
    bool p;
    string s;
    primes[0] = 2;
    pcount = 1;
    for(i=0;i<MAXP/2;i++){
        numbers[i] = 0;
    }
    for(i=0;i<MAXP/2;i++){
        if(numbers[i] == 0){
            primes[pcount] = 2*i+3;
            pcount++;
            for(j=3*i+3;j<MAXP/2;j+=2*i+3){
                numbers[j] = 1;
            }
        }
    }
    for(j = scanf("%d",&n); j != EOF; j = scanf("%d",&n)){
        printf("%d is ",n);
        p = true;
        for(i=0;primes[i]<=sqrt(n) && p && i<pcount;i++){
            if(n%primes[i]==0){
                p=false;
            }
        }
        if(p && n>1){
            s = to_string(n);
            reverse(s.begin(),s.end());
            while(s[0] == '0'){
                s = s.substr(1);
            }
            nc = n;
            n = stoi(s);
            p = nc != n;
            for(i=0;primes[i]<=sqrt(n) && p && i<pcount;i++){
                if(n%primes[i]==0){
                    p=false;
                }
            }
            if(p){
               printf("emirp.\n");
            }
            else{
                printf("prime.\n");
            }
        }
        else{
            printf("not prime.\n");
        }
    }
    return 0;
}
