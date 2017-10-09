#include <stdio.h>

int main(){
  int N,V,min,c,i;
  scanf("%i",&N);
  for(i=0;i<N;i++){
    min = 0;
    scanf("%i",&V);
    for(;V>0;V--){
      scanf("%i",&c);
      if(c>min){
	min = c;
      }
    }
    printf("Case %i: %i\n",i+1,min);
  }
  return 0;
}
