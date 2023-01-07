import csv
from re import A
import requests
from dagster import asset, AssetIn

@asset
def restaurants():
    restaurants =[
        {
            "nombre": "Casa de Campo",
            "especialidades": [
                "Pique Macho",
                "Pique Lobo",
                "Picantes"
            ],
            "telefono": "4243937",
            "direccion": {
                "calle": "Pasaje Boulevard de la Recoleta",
                "numero": "618"
            }
        },
        {
            "nombre": "Doña Fely",
            "especialidades": [
                "Chorizo Chuquisaqueño",
                "Puchero",
                "Ranga",
                "Fricase",
                "Menudito",
                "Picantes"
            ],
            "telefono": "4582972",
            "direccion": {
                "calle": "Tumusla entre Calama y Ladislao Cabrera",
                "numero": "544"
            }
        },
        {
            "nombre": "Doña Pola",
            "especialidades": [
                "Escabeche",
                "Enrollado",
                "Chicharrón",
                "Humintas"
            ],
            "telefono": "4281015",
            "direccion": {
                "calle": "Av. América esq. Av. Gualberto Villarroel",
                "numero": "275"
            }
        },
        {
            "nombre": "Jacarandá",
            "especialidades": [
                "Pique Macho",
                "Charque",
                "Picante de Lengua"
            ],
            "telefono": "4286424",
            "direccion": {
                "calle": "Av. Tadeo Haenke",
                "numero": "2150"
            }
        },
        {
            "nombre": "La Gaviota",
            "especialidades": [
                "Buffet Criollo",
                "Intendente",
                "Matambre",
                "Picante de Lengua",
                "Habas Pejtu",
                "Plato del Bicentenario"
            ],
            "telefono": "4424497",
            "direccion": {
                "calle": "C. Azanaqueo. Av. América Oeste final",
                "numero": "1000"
            }
        },
        {
            "nombre": "Felicidad",
            "especialidades": [
                "Fideos Uchu",
                "Picante de Pollo",
                "Variedad de Chichas"
            ],
            "telefono": "4446591",
            "direccion": {
                "calle": "Av. Beneméritos del Chaco, lado puente Killman"
            }
        },
        {
            "nombre": "Tunari",
            "especialidades": [
                "Chorizo Criollo",
                "Ranga",
                "Sopa de maní",
                "Riñón",
                "Lomo"
            ],
            "telefono": "4528588",
            "direccion": {
                "calle": "Av. Ballivian",
                "numero": "676"
            }
        },
        {
            "nombre": "Miraflores",
            "especialidades": [
                "Pique Macho",
                "Lechón"
            ],
            "telefono": "4248780",
            "direccion": {
                "calle": "c. Tarija casi Av. Aniceto Padilla"
            }
        },
        {
            "nombre": "Todo al Horno",
            "especialidades": [
                "Lechon",
                "Pato",
                "Pollo",
                "Pavo al horno"
            ],
            "telefono": "4409347",
            "direccion": {
                "calle": "Av. Melchor Pérez de Olguín esq. Nueva Castilla",
                "numero": "2114"
            }
        },
        {
            "nombre": "El Palmar",
            "especialidades": [
                "Lapping",
                "Pampaku"
            ],
            "telefono": "4246224",
            "direccion": {
                "calle": "c. Man Césped entre Tarcos y Algarrobos",
                "numero": "549"
            }
        }
        ]    
    return restaurants
    
@asset
def restaurants_with_5_specialties(restaurants):
    """restaurants with 5 or more specialties"""
    return [row for row in restaurants if len(row["especialidades"]) > 5]

@asset
def restaurants_located_in_avenues(restaurants):
    """restaurants located in an avenue"""
    #isinstance(row, str) and row.startswith('Av.')
    return [row for row in restaurants if "Av." in row["direccion"]["calle"]]

@asset
def restaurants_without_phone_info(restaurants):
    """restaurants without a telephone number"""
    return [item for item in restaurants if "numero" not in item["direccion"] ]

