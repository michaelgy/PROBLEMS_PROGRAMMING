#include <stdio.h>

int main(){
  int n,p,Met,met,i,j,f;
  float Price,price;
  char Name[82],name[82];
  scanf("%i %i%*[ \n]",&n,&p);
  f = 0;
  while(n != 0 && p != 0){
    if(f){
      printf("\n");
    }
    f++;
    for(i=0;i<82;i++){
      Name[i] = '\0';
      name[i] = '\0';
    }
    for(i=0;i<n;i++){
      scanf("%*[^\n]%*c");
    }
    scanf("%[^\n]",Name);
    scanf("%f %i%*[ \n]",&Price,&Met);
    for(i=0;i<Met;i++){
      scanf("%*[^\n]%*c");
    }
    for(i=1;i<p;i++){
      scanf("%[^\n]%*c",name);
      scanf("%f %i%*[ \n]",&price,&met);
      if(met>Met || (met == Met && price<Price)){
	Met = met;
	Price = price;
	for(j=0;j<82;j++){
	  Name[j] = name[j];
	}
      }
     for(j=0;j<met;j++){
       scanf("%*[^\n]%*c");
     }
     for(j=0;j<82;j++){
       name[j] = '\0';
     }
    }
    printf("RFP #%i\n%s\n",f,Name);
    scanf("%i %i%*[ \n]",&n,&p);
  }
  return 0;
}
