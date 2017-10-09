#include <stdio.h>
#include <stdlib.h>

int main(){
  int k,result;
  div_t divr;
  while(scanf("%i %i",&(divr.quot),&k) == 2){
    result = divr.quot;
    while (divr.quot>=k){
      divr = div(divr.quot,k);
      result += divr.quot;
      divr.quot += divr.rem;
    }
    printf("%i\n",result);
  }
  return 0;
}
