#include <stdio.h>
#include <ctype.h>

int main(){
  char word[100];
  int n,ac_char;
  n = 0;
  ac_char = getchar();
  while(ac_char != EOF){
    if(isspace(ac_char)){
      for(;n>0;n--){
	putchar((int) word[n-1]);
      }
      putchar(ac_char);
    }
    else{
      word[n] = (char) ac_char;
      n++;
    }
    ac_char = getchar();
  }
  return 0;
}
