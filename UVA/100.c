#include <stdio.h>

int cycle_length(int n){
  int k;
  for(k=1;n>1;k++){
    if(n%2 == 0){
      n /= 2;
    }
    else{
      n = 3*n+1;
    }
  }
  return k;
}

int max_cycle_length(int i, int j){
  int mcl, greater, less,cl;
  greater = (i-j)>0 ? i:j;
  less = (greater == i) ? j:i;
  for(mcl = 0;greater >= less; greater--){
    cl = cycle_length(greater);
    if(mcl<cl){
      mcl = cl;
    }
  }
  return mcl;
}

int main(){
  int i,j;
  while(scanf("%i %i",&i,&j) == 2){
    printf("%i %i %i\n", i,j,max_cycle_length(i,j));
  }
  return 0;
}
