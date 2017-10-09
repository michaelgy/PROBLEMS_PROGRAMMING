#include <stdio.h>

int main(){
  int ci;
  char c;
  ci = getchar();
  while(ci != EOF){
    c = (char) ci;
    printf("%c",c);
    ci = getchar();
  }
  return 0;
}
