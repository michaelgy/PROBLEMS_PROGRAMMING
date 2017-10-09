#include <stdio.h>

int main(){
  int n,W,L,H,i;
  scanf("%i",&n);
  for(i=0;i<n;i++){
    scanf("%i %i %i",&L,&W,&H);
    printf("Case %i: %s\n",i+1, (L<21 && W<21 && H<21) ? "good":"bad");
  }
  return 0;
}
