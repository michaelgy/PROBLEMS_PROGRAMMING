#include <stdio.h>

int main(){
  unsigned long long int n,m,k;
  scanf("%lli",&k);
  while(k>0){
    scanf("%lli %lli",&n,&m);
    printf("%lli\n",(n/3)*(m/3));
    k--;
  }
  return 0;
}
