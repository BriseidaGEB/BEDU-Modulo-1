#RETO 3

#¿Cuántos registros hay por cada uno de los puestos?
SELECT nombre, count(*) AS registros FROM puesto GROUP BY nombre;

#¿Cuánto dinero se paga en total por puesto?
SELECT nombre, sum(salario) AS pago_total FROM puesto GROUP BY nombre;

#¿Cuál es el número total de ventas por vendedor?
SELECT id_empleado, count(*) AS Total FROM venta GROUP BY id_empleado;

#¿Cuál es el número total de ventas por artículo?
SELECT id_articulo, count(*) AS Total FROM venta GROUP BY id_articulo;