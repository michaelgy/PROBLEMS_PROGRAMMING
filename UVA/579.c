#include <stdio.h>
int main(){
  int hh,mm;
  float a;
  for(scanf("%d:%d",&hh,&mm);mm!= 0 || hh!=0;scanf("%d:%d",&hh,&mm)){
    a = 30*(hh%12)-(5.5)*mm;
    a = a>=0?a:-a;
    a = a>180?360-a:a;
    printf("%.3f\n",a );
  }
  return 0;
}
