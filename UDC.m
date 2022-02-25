clc;clear;

try
  pkg load database
  conn = pq_connect(setdbopts('dbname','Edad','host','localhost','port','5432','user','postgres','password','Paco0109'))
  fprintf('Determinar unidades, decenas, centenas del numero \n');
  n1=input('Ingrese un numero entre 0 y 999: ');
  
  if (n1<=999)&&(n1>=0)
    c=fix(n1/100);
    d=fix((n1 - c*100)/10);
    u=fix(n1-c*100-d*10);
    printf('El numero tiene \n');
    printf('Centenas = %i \n', c);
    printf('Decenas = %i \n', d);
    printf('Unidades = %i \n', u);
    N = pq_exec_params(conn,"insert into udc(numero, centenas, decenas, unidades) values($1,$2,$3,$4);",{n1,c,d,u});
  else 
    printf('Ingrese un numero en el intervalo indicado');
  endif

catch
 printf('Ha ocurrido un error' \n);
end_try_catch
