#include <stdio.h>

int dcc(int x, int y){
  x = y-x;
  x = (x>-1) ? x: x+40;
  return x;
}

int solution(int p, int a, int b, int c){
  int sol,d1,d2,d3;
  sol = 1080;
  d1 = dcc(p,a);
  d2 = dcc(a,b);
  d3 = dcc(b,c);
  d1 = (d1 == 0 )? 0: 40-d1;
  d3 = (d3 == 0) ? 0: 40-d3;
  return sol+d1*9+d2*9+d3*9;
}


int main(){
  int p, a, b, c;
  scanf("%i %i %i %i",&p,&a,&b,&c);
  while(p!=0 || a!= 0 || b!=0 || c!=0){
    printf("%i\n",solution(p,a,b,c));
    scanf("%i %i %i %i",&p,&a,&b,&c);
  }
  return 0;
}
