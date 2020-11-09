#Obtener el puesto de un empleado
CREATE VIEW Emp_pues_BGEB AS
SELECT concat(e.nombre,' ',apellido_paterno) AS Nombre, p.nombre AS puesto FROM empleado AS e
JOIN puesto AS p
ON e.id_puesto = p.id_puesto;

SELECT * FROM Emp_pues_BGEB;

#Saber qué artículos ha vendido cada empleado
CREATE VIEW Emp_Art_BGEB AS
SELECT clave, concat(emp.nombre,' ',apellido_paterno) AS nombre, art.nombre AS Articulos FROM venta AS ven
JOIN articulo AS art 
ON ven.id_articulo = art.id_articulo 
JOIN empleado AS emp
ON emp.id_empleado = ven.id_empleado
ORDER BY clave; 

SELECT * FROM Emp_Art_BGEB;

#Saber qué puesto ha tenido más ventas
CREATE VIEW Pues_vent_BGEB AS
SELECT p.nombre, count(v.clave) Total FROM venta AS v
JOIN empleado AS e
ON v.id_empleado = e.id_empleado
JOIN puesto AS p
ON e.id_puesto = p.id_puesto
GROUP BY p.nombre
ORDER BY Total Desc;

SELECT * FROM Pues_vent_BGEB LIMIT 1;