#include <stdio.h>

int main(){
  long int a,b;
  int n;
  scanf("%i",&n);
  while(n>0){
    scanf("%li %li",&a,&b);
    a -= b;
    if(a==0){
      putchar((int) '=');
    }
    else if(a>0){
      putchar((int) '>');
    }
    else{
      putchar((int) '<');
    }
    putchar((int) '\n');
    n--;
  }
  return 0;
}
