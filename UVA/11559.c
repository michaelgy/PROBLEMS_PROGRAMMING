#include <stdio.h>

int main(){
  int N,B,H,W,p,pmin,a,i;
  while(scanf("%i %i %i %i",&N,&B,&H,&W)== 4){
    pmin = 10001;
    while(H>0){
      scanf("%i",&p);
      for(i=0;i<W;i++){
        if(p<pmin){
          scanf("%i",&a);
          if(a>=N){
            pmin = p;
          }
        }
        else{
          scanf("%*i");
        }
      }
      H--;
    }
    if(pmin*N >B){
      printf("stay home\n");
    }
    else{
      printf("%i\n",pmin*N);
    }
  }
  return 0;
}
