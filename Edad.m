clc;clear;

try
  pkg load database
  conn = pq_connect(setdbopts('dbname','Edad','host','localhost','port','5432','user','postgres','password','Paco0109'))
  fprintf('Calcular la edad y saber si ya ha cumplido años \n');
  d = input('Ingrese dia de su nacimiento: ');
  m = input('Ingrese mes de su nacimiento: ');
  y = input('Ingrese año de su nacimiento: ');
  edad=2022-y;
  
  if (m<=2)
    printf('Usted ya cumplio %i años', edad);
    concat=strcat('Usted nacio el dia', num2str(d), 'del mes', num2str(m), 'del año', num2str(y));
    concat1=strcat('Cumplio', num2str(edad), 'años');
    N = pq_exec_params(conn,"insert into datos(actual_año, cumpleaños) values($1,$2);",{edad, 'Ya cumplio años'});
  elseif 
    printf('Usted cumplira %i años', edad);
    edad1=2021-y;
    concat=strcat('Usted nacio el dia', num2str(d), 'del mes', num2str(m), 'del año', num2str(y));
    concat1=strcat('Cumplira', num2str(edad), 'años');
    N = pq_exec_params(conn,"insert into datos(actual_año, cumpleaños) values($1,$2);",{edad1, 'No ha cumplido años'});
  endif
  

  
catch
  printf("Ha ocurrido un error")
end_try_catch
