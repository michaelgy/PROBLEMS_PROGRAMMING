#include <stdio.h>

long long int nth_ugly(int n){
  int count,n2,n3,n5;
  long long int ugly,tmp;
  count = 2;
  ugly = 2;
  while(count < n){
    ugly++;
    tmp = ugly;
    n2 = 0;
    n3 = 0;
    n5 = 0;
    while( ugly%2 == 0){
      ugly /= 2;
      n2++;
    }
    while( ugly%3 == 0){
      ugly /= 3;
      n3++;
    }
    while( ugly%5 ==0 ){
      ugly /= 5;
      n5++;
    }
    if(ugly == 1){
      count++;
    }
    ugly = tmp;
  }
  return ugly;
}
int main(){
  long long int ugly;
  ugly = 859963392; /* nth_ugly(1500);*/
  printf("The 1500'th ugly number is %lli.\n",ugly);
  return 0;
}
