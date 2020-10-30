#RETO 2
#¿Cuál es el promedio de salario de los puestos?
SELECT avg(salario) AS promedio FROM puesto;

#¿Cuántos artículos incluyen la palabra Pasta en su nombre?
SELECT count(*) AS Total FROM articulo WHERE nombre LIKE '%Pasta%';

#¿Cuál es el salario mínimo y máximo?
SELECT min(salario) AS SALARIO_MIN, max(salario) AS SALARIO_MAX FROM puesto;

#¿Cuál es la suma del salario de los últimos cinco puestos agregados?
SELECT count(*) AS Num_puestos FROM puesto; #Num_puestos=1000
SELECT SUM(salario) AS SUMA FROM puesto WHERE id_puesto > 995;


