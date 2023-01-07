import csv
from re import A
import requests
from dagster import asset, AssetIn
from bs4 import BeautifulSoup

'''

import sys
sys.setrecursionlimit(10000)

HEADER_ROW = 0
MASS_ROW = 1
DENSITY_ROW = 3
GRAVITY_ROW = 4
LENGTH_OF_DAY = 7

response = requests.get("http://localhost:8000/Planetary_Fact_Sheet.html")
pagina = BeautifulSoup(response.text, "html.parser" )

@asset(group_name="planetas")
def PageInfo():
    row_headers = pagina.body.find_all(name="td", attrs={"align":"left"})
    return row_headers

def extract_numbers(row_headers, row_number):
    tds = row_headers[row_number].find_parent().find_all(name="td", attrs={"align":"center"})
    return [float(td.text) for td in tds]

def extract_headers(row_headers):
    tds = row_headers[HEADER_ROW].find_parent().find_all(name="td", attrs={"align":"center"})
    return [td.find("a").text for td in tds]

@asset(group_name="planetas")
def namesRow(PageInfo):
    names = extract_headers(PageInfo)
    return names 


#@asset(group_name="planetas")
#def typeOfInfoRow(PageInfo):
   # extracted_Data = extract_numbers(PageInfo, HEADER_ROW)
   # return extracted_Data

@asset(group_name="planetas")
def massRow(PageInfo):
    extracted_Data = extract_numbers(PageInfo, MASS_ROW)
    return extracted_Data

@asset(group_name="planetas")
def densityRow(PageInfo):
    extracted_Data = extract_numbers(PageInfo, DENSITY_ROW)
    return extracted_Data

@asset(group_name="planetas")
def gravityRow(PageInfo):
    extracted_Data = extract_numbers(PageInfo, GRAVITY_ROW)
    return extracted_Data

@asset(group_name="planetas")
def lengthOfDayRow(PageInfo):
    extracted_Data = extract_numbers(PageInfo, LENGTH_OF_DAY)
    return extracted_Data


@asset(group_name="planetas")
def getAllExtractedInfo(namesRow, massRow, densityRow, gravityRow, lengthOfDayRow):
    list_of_lists = [namesRow, massRow, densityRow, gravityRow, lengthOfDayRow]
    planet_dictionary = {z[0]: list(z[1:]) for z in zip(*list_of_lists)} 
    return planet_dictionary


@asset(group_name="planetas")
def planets_with_most_day_length(getAllExtractedInfo):
    marklist = sorted(getAllExtractedInfo.items(), key=lambda x:x[1][3], reverse=True)
    return marklist[:3]

@asset(group_name="planetas")
def planets_with_less_mass_than_earth(getAllExtractedInfo):
    marklist = sorted(getAllExtractedInfo.items(), key=lambda x:x[1][0])
    sortdict = dict(marklist)
    if 'EARTH' in sortdict:
        index = list(sortdict).index('EARTH')
    return marklist[:index]

    
    '''