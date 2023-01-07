from dagster_data_app.jobs.ip_job import *

def test_get_total_size():
    res = IpsJob.execute_in_process()
    assert res.success

def test_get_Ips():
    IpxTXT=ipsFromTxt()
    IpsJSON=getJsonFromIps(IpxTXT)
    ips=getIps(IpsJSON)
    result = ips[0]
    assert result == "181.65.208.173"

def test_get_Continent():
    IpxTXT=ipsFromTxt()
    IpsJSON=getJsonFromIps(IpxTXT)
    ips=getContinent(IpsJSON)
    result = ips[0]
    assert result == "South America"

def test_get_Country():
    IpxTXT=ipsFromTxt()
    IpsJSON=getJsonFromIps(IpxTXT)
    ips=getCountry(IpsJSON)
    result = ips[0]
    assert result == "Peru"

def test_get_Region():
    IpxTXT=ipsFromTxt()
    IpsJSON=getJsonFromIps(IpxTXT)
    ips=getRegion(IpsJSON)
    result = ips[0]
    assert result == "Lima"

def test_get_City():
    IpxTXT=ipsFromTxt()
    IpsJSON=getJsonFromIps(IpxTXT)
    ips=getCity(IpsJSON)
    result = ips[0]
    assert result == "Lima District"

def test_get_Isp():
    IpxTXT=ipsFromTxt()
    IpsJSON=getJsonFromIps(IpxTXT)
    ips=getIsp(IpsJSON)
    result = ips[0]
    assert result == "Telefonica del Peru S.A.A."

def test_get_Currency():
    IpxTXT=ipsFromTxt()
    IpsJSON=getJsonFromIps(IpxTXT)
    ips=getCurrency(IpsJSON)
    result = ips[0]
    assert result == "Peruvian Nuevo Sol"