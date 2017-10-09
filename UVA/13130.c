#include <stdio.h>

int main(){
  int N,c,n,i;
  _Bool scala;
  scanf("%i",&N);
  for(;N>0;N--){
    scala = 1;
    scanf("%i",&c);
    for(i=4;i>0;i--){
      scanf("%i",&n);
      if( n != c+1){
	scala = 0;
      }
      c = n;
    }
    putchar(scala ? 'Y':'N');
    putchar('\n');

  }
  return 0;
}
