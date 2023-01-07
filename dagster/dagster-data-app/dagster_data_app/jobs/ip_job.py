import csv
from re import A
import requests
from dagster import asset, AssetIn, job, op


import csv


@op
def ipsFromTxt():
    ips = []
    with open('C:/Users/chris/Downloads/operaciones_y_jobs(2)/lista_direcciones_ip.txt') as f:
        [ips.append(line.strip()) for line in f.readlines()]
    f.close()
    return ips

@op
def getJsonFromIps(ipsFromTxt):
    requestURL = "http://free.ipwhois.io/json/"
    request = []
    for ip in ipsFromTxt:
        addedURL = requestURL + ip
        response = requests.get(addedURL)
        request.append(response.json())
    return request

@op
def getIps(getJsonFromIps):
    infoExtracted = []
    for ipInfo in getJsonFromIps:
        infoExtracted.append(ipInfo['ip'])
    return infoExtracted

@op
def getContinent(getJsonFromIps):
    infoExtracted = []
    for ipInfo in getJsonFromIps:
        infoExtracted.append(ipInfo['continent'])
    return infoExtracted

@op
def getCountry(getJsonFromIps):
    infoExtracted = []
    for ipInfo in getJsonFromIps:
        infoExtracted.append(ipInfo['country'])
    return infoExtracted

@op
def getRegion(getJsonFromIps):
    infoExtracted = []
    for ipInfo in getJsonFromIps:
        infoExtracted.append(ipInfo['region'])
    return infoExtracted

@op
def getCity(getJsonFromIps):
    infoExtracted = []
    for ipInfo in getJsonFromIps:
        infoExtracted.append(ipInfo['city'])
    return infoExtracted

@op
def getIsp(getJsonFromIps):
    infoExtracted = []
    for ipInfo in getJsonFromIps:
        infoExtracted.append(ipInfo['isp'])
    return infoExtracted

@op
def getCurrency(getJsonFromIps):
    infoExtracted = []
    for ipInfo in getJsonFromIps:
        infoExtracted.append(ipInfo['currency'])
    return infoExtracted

def saveToCSV(Header,Rows,CSVName):
    with open(CSVName, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=Header)
        writer.writeheader()
        writer.writerows(Rows)

@op
def saveInfoToCSV(getIps, getContinent, getCountry, getRegion, getCity, getIsp, getCurrency):
    tuples = list(zip(getIps, getContinent, getCountry, getRegion, getCity, getIsp, getCurrency))
    records = [{"ip":t[0], "continent": t[1], "country": t[2],
                "region":t[3], "city": t[4], "isp": t[5], "currency": t[6]} for t in tuples]
    saveToCSV(records[0].keys(),records,"IpInfo.csv")


@job
def IpsJob():
    IpxTXT=ipsFromTxt()
    IpsJSON=getJsonFromIps(IpxTXT)
    ips=getIps(IpsJSON)
    continents=getContinent(IpsJSON)
    countries=getCountry(IpsJSON)
    regions=getRegion(IpsJSON)
    cities=getCity(IpsJSON)
    isps=getIsp(IpsJSON)
    currency=c(IpsJSON)
    saveInfoToCSV(ips,continents,countries,regions,cities,isps,currency)

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