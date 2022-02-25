clc;clear;

try
  pkg load database
  conn = pq_connect(setdbopts('dbname','Edad','host','localhost','port','5432','user','postgres','password','Paco0109'))
  fprintf('Juego del gran 8 \n');
  I1 = input('Ingrese tu numero de la suerte para tirar los dados: ');
  A = randi(6,1);
  B = randi(6,1);
  C = A+B;
  
  if(C==8)
    printf('obtuviste un %i en el primer dado \n' , A);
    printf('obtuviste un %i en el segundo dado \n', B);
    printf('Tienes un %i en total, ganaste \n', C);
    N = pq_exec_params(conn,"insert into juego(numero_obtenido, resultado) values($1,$2);",{C, 'Has ganado'});
    
  elseif (C==7)
    printf('obtuviste un %i en el primer dado \n', A);
    printf('obtuviste un %i en el segundo dado \n', B);
    printf('Tienes un %i en total, Perdiste \n', C);
    N = pq_exec_params(conn,"insert into juego(numero_obtenido, resultado) values($1,$2);",{C, 'Has perdido'});
    
  else 
    printf('obtuviste un %i en el primer dado \n', A);
    printf('obtuviste un %i en el segundo dado \n', B);
    printf('Tienes un %i en total, Vuelve a tirar \n', C);
    N = pq_exec_params(conn,"insert into juego(numero_obtenido, resultado) values($1,$2);",{C, 'Vuelve a tirar'});
  endif
  
catch
  printf("Ha ocurrido un error \n")
end_try_catch
  