#include <stdio.h>
#include <math.h>
#include <malloc.h>

/* Funcion para hallar el cincumcentro dados los 3 puntos, la sacamos de wikipedia*/
double * circumcenter(double p[3][2]){
  double ux,uy,d,pw[3],*result;
  int i;
  for(i=0;i<3;i++){
    pw[i] = pow(p[i][0],2)+pow(p[i][1],2);
  }
  for(i=0;i<3;i++){
    ux += pw[i]*(p[(i+1)%3][1]-p[(i+2)%3][1]);
    uy += pw[i]*(p[(i+2)%3][0]-p[(i+1)%3][0]);
    d += p[i][0]*(p[(i+1)%3][1]-p[(i+2)%3][1]);
  }
  ux /= 2*d;
  uy /= 2*d;
  result = (double *)malloc(sizeof(double)*2);
  result[0] = ux;
  result[1] = uy;
  return result;
}


/* Funcion para encontrar el minimo rectangulo, recibe los 3 puntos p, la cantidad de lados n y el numero del poligono k
dados los 3 puntos, halla el cincumcentro, luego toma uno de los puntos y centra el punto en el origen,
a partir del punto centrado, se construyen los demas puntos, en cada punto construido hallamos las coordenadas (x,y) y 
verificamos si las coordenadas son el minimo x o el maximo x, el minimo y o el maximo y, como sea el caso. Al final
dados los puntos minimos y maximos se hallan las distancias en las coordenadas correspondientes y se imprime el area
*/

void sra(double p[3][2],int n, int k){
  double *center,px,py,px0,py0,angle,minx,miny,maxx,maxy,r,fangle;
  center = circumcenter(p);
  px0 = p[0][0]-center[0];
  py0 = p[0][1]-center[1];
  r = sqrt(pow(px0,2)+pow(py0,2));
  minx = px0;
  maxx = px0;
  miny = py0;
  maxy = py0;
  angle = 2*M_PI/(double)n;
  fangle = acos(fabs(px0)/r);
  if (px0 >= 0 && py0 <= 0){
    fangle += M_PI/(double)2;
  }
  if (px0 <= 0 && py0 >= 0){
    fangle += M_PI;
  }
  if (px0 <= 0 && py0 >= 0){
    fangle += 3* M_PI/((double)2);
  }
    
  for(;n>0;n--){
    px = r*cos(fangle+n*angle);
    py = r*sin(fangle+n*angle);
    minx = px<minx?px:minx;
    maxx = px>maxx?px:maxx;
    miny = py<miny?py:miny;
    maxy = py>maxy?py:maxy;
  }
  minx = fabs(maxx-minx);
  miny = fabs(maxy-miny);
  printf("Polygon %i: %.3lf\n",k,minx*miny);
}

/* Solo lee la entrada y se lo entrega a la funcion sra*/
int main(){
  int n,i,k;
  double p[3][2],*result;
  k = 0;
  for(scanf("%i",&n);n>0;scanf("%i",&n)){
    k++;
    for(i=0;i<3;i++){
      scanf("%lf %lf",p[i],p[i]+1);
    }
    result = circumcenter(p);
    sra(p,n,k);
  }
  return 0;
} 
