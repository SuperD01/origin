clc;clear;

pkg load database
conn = pq_connect(setdbopts('dbname','Edad','host','localhost','port','5432','user','postgres','password','Paco0109'))

a = input('Inserte �ngulo en grados: a = '); fprintf('\n');
b = input('Inserte �ngulo en grados: b = '); fprintf('\n');

c = 180 - (a + b);
fprintf('�ngulo en grados: c = %.2f\n\n', c);

N = pq_exec_params(conn,"insert into angulos(primer_angulo, segundo_angulo, angulo_resultante) values($1,$2,$3);",{a, b, c});