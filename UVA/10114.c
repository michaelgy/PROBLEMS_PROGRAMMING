#include <stdio.h>

int main(){
  int months,drecords,mdepre,m;
  float dpayment, loan, carw, depre,pdepre;
  scanf("%i %f %f %i",&months,&dpayment,&loan,&drecords);
  while(months>0){
    scanf("%i %f",&m, &pdepre);
    carw = (dpayment+loan)*(1-pdepre);
    m++;
    printf("car worth:%f       loan:%f\n",carw,loan);
    for(drecords--;drecords>0;drecords--){
      scanf("%i %f",&mdepre,&depre);
      while(mdepre>m && loan>=carw){
        m++;
        carw *= 1-pdepre;
        loan -= dpayment;
        printf("car worth:%f       loan:%f\n",carw,loan);
      }
      if(mdepre == m){
        pdepre = depre;
      }
    }
    while(loan >= carw && m<=months){
      
      carw *= 1-pdepre;
      loan -= dpayment;
      m++;
      printf("--car worth:%f       loan:%f\n",carw,loan);
    }
    printf(m==1?"%i month\n":"%i months\n",m-1);
    scanf("%i %f %f %i",&months,&dpayment,&loan,&drecords);
  }
  return 0;
}
