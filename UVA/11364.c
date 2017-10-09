#include <stdio.h>

int main(){
  int n, shops,i,minx,maxx,pos;
  scanf("%i",&n);
  while(n>0){
    scanf("%i",&shops);
    scanf("%i",&minx);
    maxx = minx;
    for(i = 1; i<shops; i++){
      scanf("%i",&pos);
      maxx = pos>maxx ? pos: maxx;
      minx = pos<minx ? pos: minx;
    }
    printf("%i\n",(maxx-minx)*2);
    n--;
  }
  return 0;
}
