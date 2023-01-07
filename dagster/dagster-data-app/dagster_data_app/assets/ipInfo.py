import csv
from re import A
import requests
from dagster import asset, AssetIn

from bs4 import BeautifulSoup
import json

@asset(group_name="ipInformation")
def ipsFromTxt():
    ips = []
    with open('C:/Tareas/2022/SisInfo3/tema 3/05/lista_direcciones_ip.txt') as f:
        [ips.append(line.strip()) for line in f.readlines()]
    f.close()
    return ips

@asset(group_name="ipInformation")
def getJsonFromIps(ipsFromTxt):
    requestURL = "http://free.ipwhois.io/json/"
    request = []
    for ip in ipsFromTxt:
        addedURL = requestURL + ip
        response = requests.get(addedURL)
        request.append(response.json())
    return request

@asset(group_name="ipInformation")
def Ips(getJsonFromIps):
    infoExtracted = []
    for ipInfo in getJsonFromIps:
        infoExtracted.append(ipInfo['ip'])
    return infoExtracted

@asset(group_name="ipInformation")
def Continent(getJsonFromIps):
    infoExtracted = []
    for ipInfo in getJsonFromIps:
        infoExtracted.append(ipInfo['continent'])
    return infoExtracted

@asset(group_name="ipInformation")
def Country(getJsonFromIps):
    infoExtracted = []
    for ipInfo in getJsonFromIps:
        infoExtracted.append(ipInfo['country'])
    return infoExtracted

@asset(group_name="ipInformation")
def Region(getJsonFromIps):
    infoExtracted = []
    for ipInfo in getJsonFromIps:
        infoExtracted.append(ipInfo['region'])
    return infoExtracted

@asset(group_name="ipInformation")
def City(getJsonFromIps):
    infoExtracted = []
    for ipInfo in getJsonFromIps:
        infoExtracted.append(ipInfo['city'])
    return infoExtracted

@asset(group_name="ipInformation")
def Isp(getJsonFromIps):
    infoExtracted = []
    for ipInfo in getJsonFromIps:
        infoExtracted.append(ipInfo['isp'])
    return infoExtracted

@asset(group_name="ipInformation")
def Currency(getJsonFromIps):
    infoExtracted = []
    for ipInfo in getJsonFromIps:
        infoExtracted.append(ipInfo['currency'])
    return infoExtracted

import csv
def saveToCSV(Header,Rows,CSVName):
    with open(CSVName, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=Header)
        writer.writeheader()
        writer.writerows(Rows)

@asset(group_name="ipInformation")
def saveInfoToCSV(Ips, Continent, Country, Region, City, Isp, Currency):
    tuples = list(zip(Ips, Continent, Country, Region, City, Isp, Currency))
    records = [{"ip":t[0], "continent": t[1], "country": t[2],
                "region":t[3], "city": t[4], "isp": t[5], "currency": t[6]} for t in tuples]
    saveToCSV(records[0].keys(),records,"IpInfo.csv")

'''
1. ip 
2. continent
3. country
4. region
5. city
6. isp
7. currency
'''
#http://free.ipwhois.io/json/<direccion-ip>