import requests
from bs4 import BeautifulSoup
from dagster import asset, AssetIn


@asset(group_name="holidays")
def country_data():
    
    """
    Desde https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent_(data_file)
    extraer una lista de diccionarios con el código de dos letras y el nombre del país únicamente de los países de
    América del Sur (CC='SA')
    """

    return [{"code": "BO", "country": "Bolivia, Plurinational State of"}]


@asset(group_name="holidays")
def holiday_data(country_data):
    """
    Para cada país en el parámetro de entrada. Emplear 'code'
    para extraer la lista de feriados empleando el siguiente servicio
    https://date.nager.at/api/v2/publicholidays/2022/<code>
    """
    https_String = "https://date.nager.at/api/v2/publicholidays/2022/"
    holidays = []
    for country in country_data:
        holidays.extend(extract_holiday_data(country))

    return holidays

def get_Name_Info(country):
    infoExtracted = []
    for info in country:
        infoExtracted.append(country['name'])
    return infoExtracted

@asset(group_name="holidays")
def save_holiday_data(holiday_data) -> None:
    """
    Guardar los datos en un archivo holiday_data.csv con los siguientes datos sobre los feriados
    - country
    - code
    - date
    - name
    """
    tuples = list(zip(country_Info, code_Info, date_Info, name_Info))
    records = [{"country":t[0], "code": t[1], "date": t[2],"name":t[3]} for t in tuples]
    saveToCSV(records[0].keys(),records,"IpInfo.csv")
    pass

import csv
def saveToCSV(Header,Rows,CSVName):
    with open(CSVName, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=Header)
        writer.writeheader()
        writer.writerows(Rows)

# helper functions
#def extract_holiday_data(country):
    # Llamar al servicio en esta función
    # Si el servicio NO retorna response.status_code == 200
    # se retorna una lista vacía.
    #https_string = "https://date.nager.at/api/v2/publicholidays/2022/"
    #country_code_string = country

   # return [{"country": "Bolivia, Plurinational State of", "code": "BO", "date": "2022-01-01", "name": "Año Nuevo"}]

def extract_holiday_data(country):
    https_string = "https://date.nager.at/api/v2/publicholidays/2022/"
    country_code_string = country["code"]
    response = requests.get(https_string + country_code_string)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return []