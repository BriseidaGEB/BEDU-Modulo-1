#¿Cuál es el nombre de los empleados que realizaron cada venta?
SELECT clave, nombre, apellido_paterno FROM venta AS ven 
INNER JOIN empleado AS emp
ON emp.id_empleado = ven.id_empleado
ORDER BY clave;

#¿Cuál es el nombre de los artículos que se han vendido?
SELECT ven.clave, art.nombre FROM venta AS ven
INNER JOIN articulo AS art
ON ven.id_articulo = art.id_articulo
ORDER BY clave;

#¿Cuál es el total de cada venta?
SELECT clave, round(SUM(precio),2) AS Total FROM venta AS vent
INNER JOIN articulo AS art
ON vent.id_articulo = art.id_articulo
GROUP BY clave
ORDER BY clave;