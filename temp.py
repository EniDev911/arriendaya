 
import os,django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_site.settings")
django.setup()

from arrienda_ya.models import Inmueble, Region

def get_inmuebles_by_name_and_description(name, descr):
    filter1 = {"nombre_inmueble__contains":name}
    filter2 = {"descripcion__contains":descr}
    inmuebles = Inmueble.objects.filter(**filter1).filter(**filter2)
    with open("datos.txt", "w") as xfile:
        for inmueble in inmuebles.values():
            xfile.write(str(inmueble))
            xfile.write("\n")

# get_inmuebles_by_name_and_description("Providencia", "Cocina")

def get_inmuebles_by_comuna(comuna):
    query = "SELECT inm.id, inm.nombre_inmueble, inm.descripcion"
    query += " FROM arrienda_ya_inmueble AS inm"
    query += " INNER JOIN arrienda_ya_region AS reg"
    query += " ON inm.id_region_id = reg.id"
    query += " INNER JOIN arrienda_ya_comuna AS com"
    query += " ON inm.id_comuna_id = com.id"
    query += f" WHERE com.comuna LIKE '%%{str(comuna)}%%'"

    results = Inmueble.objects.raw(query)
        
    with open("datos.txt", "w") as xfile:
        for result in results:
          xfile.write(result.nombre_inmueble+", "+result.descripcion)
          xfile.write("\n")
          
get_inmuebles_by_comuna("Bernardo")


    
