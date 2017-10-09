#include <stdio.h>

int main(){
  float  H,U,D,F,total,distance,factor;
  int n;
  scanf("%f %f %f %f",&H,&U,&D,&F);
  while(H != 0){
    total = 0;
    distance = 0;
    factor = (U*F)/100;
    for(n = 1; total <= H  && total>=0;n++){
      distance = U-factor*(n-1);
      distance = distance>0?distance:0;
      total += distance;
      if(total <= H){
	total -= D;
      }
    }
    if(total > H){
      printf("success on day %i\n",n-1);
    }
    else{
      printf("failure on day %i\n",n-1);
    }
    scanf("%f %f %f %f",&H,&U,&D,&F);
  }
  return 0;
}
 
