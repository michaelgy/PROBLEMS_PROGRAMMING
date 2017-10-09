#include <stdio.h>

int main(){
  char input[8];
  int n;
  scanf("%s",input);
  for(n=1;input[0] != '*';n++){
    printf("Case %i: Hajj-e-A",n);
    if(input[0] == 'H'){
      printf("kbar\n");
    }
    else{
      printf("sghar\n");
    }
    scanf("%s", input);
  }
  return 0;
}
