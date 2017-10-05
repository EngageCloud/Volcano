import json
import pandas
import folium
import requests


'''

#Fetch Volcano data
url = "https://www.ngdc.noaa.gov/nndc/struts/results?type_0=Like&query_0=&op_8=eq&v_8=&type_10=EXACT&query_10=None+Selected&le_2=&ge_3=&le_3=&ge_2=&op_5=eq&v_5=&op_6=eq&v_6=&op_7=eq&v_7=&t=102557&s=5&d=5"
htmlContent = requests.get(url, verify=False)

jsonD = json.dumps(htmlContent.text)
#jsonL = json.load(jsonD)

file = open("Volcanos.json", "w+")
file.write(jsonD)
'''



