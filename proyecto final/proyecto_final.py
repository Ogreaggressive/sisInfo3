import re
import requests
from bs4 import BeautifulSoup
from dagster import asset, AssetIn


@asset(group_name="mountains")
def mountain_data():
    """
    Desde http://localhost:8000/Anexo_Monta%C3%B1as%20de%20la%20cordillera%20de%20los%20Andes%20-%20Wikipedia%2C%20la%20enciclopedia%20libre.html
    extraer una lista de diccionarios con los siguientes datos: nombre, pais, altitud, latitud, longitud
    """

    return [{"name": "Aconcagua", "country": "Argentina", "altitude": 6960, "latitude": -32.650, "longitude": -70.017}
            ,{"name": "Chearoco", "country": "Bolivia", "altitude": 6127, "latitude": None, "longitude": None}]


@asset(group_name="mountains")
def generate_geojson_file(mountain_data) -> None:
    """
    Convertir la lista de diccionarios en formato GeoJson omitiendo los datos que no tiene latitud y longitud
    guardar en un archivo mountain_data.json
    """
    pass


# Helper functions

