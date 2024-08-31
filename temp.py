 
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

get_inmuebles_by_name_and_description("Providencia", "Cocina")