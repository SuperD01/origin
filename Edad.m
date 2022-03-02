clc;clear;

try
  pkg load database
  conn = pq_connect(setdbopts('dbname','Edad','host','localhost','port','5432','user','postgres','password','Paco0109'))
  fprintf('Calcular la edad y saber si ya ha cumplido a�os \n');
  d = input('Ingrese dia de su nacimiento: ');
  m = input('Ingrese mes de su nacimiento: ');
  y = input('Ingrese a�o de su nacimiento: ');
  edad=2022-y;
  
  if (m<=2)
    printf('Usted ya cumplio %i a�os', edad);
    concat=strcat('Usted nacio el dia', num2str(d), 'del mes', num2str(m), 'del a�o', num2str(y));
    concat1=strcat('Cumplio', num2str(edad), 'a�os');
    N = pq_exec_params(conn,"insert into datos(actual_a�o, cumplea�os) values($1,$2);",{edad, 'Ya cumplio a�os'});
  elseif 
    printf('Usted cumplira %i a�os', edad);
    edad1=2021-y;
    concat=strcat('Usted nacio el dia', num2str(d), 'del mes', num2str(m), 'del a�o', num2str(y));
    concat1=strcat('Cumplira', num2str(edad), 'a�os');
    N = pq_exec_params(conn,"insert into datos(actual_a�o, cumplea�os) values($1,$2);",{edad1, 'No ha cumplido a�os'});
  endif
  

  
catch
  printf("Ha ocurrido un error")
end_try_catch
