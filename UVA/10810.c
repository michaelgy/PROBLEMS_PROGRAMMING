#include <stdio.h>

#define M 500000

long merge_s(int ts[], int ax[], int a, int b){
  
  if(a == b){
    return 0;
  }
  if(b-a == 1){
    return 0;
  }
  int m,e,d,f;
  long total;
  
  m = (b+a)>>1;
  e = a;
  d = a;
  f = m;
  total = merge_s(ts,ax,a,m);
  total += merge_s(ts,ax,m,b);
  while(d<m && f<b){
    if(ts[d]<= ts[f]){
      ax[e] = ts[d];
      d+=1;
    }
    else{
      ax[e] = ts[f];
      f+=1;
      total += m-d;
    }
    e+=1;
  }
  while(d<m){
    ax[e] = ts[d];
    e++;
    d++;
  }
  while(f<b){
    ax[e] = ts[f];
    e++;
    f++;
  }
  for(d=a;d<b;d++){
    ts[d] = ax[d];
  }
  return total;
}

int main(){
  int n,ts[M],ax[M],e;
  long t;
  scanf("%d",&n);
  while(n){
    for(e=0;e<n;e++){
      scanf("%d",ts+e);
    }
    t = merge_s(ts,ax,0,n);
    printf("%ld\n",t);
    scanf("%d",&n);
  }
  return 0;
}
