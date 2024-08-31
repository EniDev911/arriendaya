SELECT inm.id, inm.nombre_inmueble, inm.descripcion
FROM arrienda_ya_inmueble AS inm
INNER JOIN arrienda_ya_region AS reg
ON inm.id_region_id = reg.id
INNER JOIN arrienda_ya_comuna AS com
ON inm.id_comuna_id = com.id
WHERE com.comuna LIKE '%Bernardo%';