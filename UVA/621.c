#include <stdio.h>
#include <ctype.h>

void decrypt(){
  char buffer[5],ch;
  int n,c,c1,c2,c3;
  c1 = 0;c2=0;c3=0;
  c = getchar();
  for(n = 0;!(isspace(c) || c == EOF);n++){
    ch = (char) c;
    if(n<5){
      buffer[n]=ch;
    }
    else{
      buffer[3] = buffer[4];
      buffer[4] = ch;
    }
    c = getchar();
  }
  if(n<3){
    c1 = 1;
  }
  else if(n==3){
    if(buffer[1] == '3'){
      c2 = 1;
    }
    else{
      c3 = 1;
    }
  }
  else if(n==4){
    if(buffer[2] == '3'){
      c2 = 1;
    }
    else if(buffer[0] == '9'){
      c3 = 1;
    };
  }
  else{
    if(buffer[4] == '5'){
      c2 = 1;
    }
    else if(buffer[0] == '9'){
      c3 = 1;
    }
  }
  if(c1){
    putchar('+');
  }
  else if(c2){
    putchar('-');
  }
  else if(c3){
    putchar('*');
  }
  else{
    putchar('?');
  }
  putchar('\n');
}
int main(){
  long long int n;
  scanf("%lli",&n);
  getchar();
  while(n>0){
    decrypt();
    n--;
  }
  return 0;
}
