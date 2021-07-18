import os
import csv

os.system("cat village_list.txt | tr [:upper:] [:lower:] >capkasaba.txt")
oo=open("capkasaba.txt","rt")
dd=csv.reader(oo)
myset=set()

for each in dd:
     myset.add(each[0])

for e in myset:
     os.system("cat appdatajuly16.csv "+"|"+" grep \""+e+"\" >>"+" kasaba.csv")


os.system(" awk -F , -v OFS='\t' 'NR == 1 || $6 > 4 {print $4}' kasaba.csv >village_lo.txt")
os.system("cat village_lo.txt | tr [:lower:] [:upper:] >village_loop.txt")

os.system(" awk -F , -v OFS='\t' 'NR == 1 || $6 > 4 {print $8}' kasaba.csv >pan_loop.txt ")


oo=open("pan_loop.txt","rt")
import csv
dd=oo.readlines()
#
for i in dd:
        lo = open("fish.txt", "a")

        if str(i)=="\n":
            print("00")
            lo.write("00"+"\n")
        else :
            print(i)
            lo.write(str(i))



oo=open("fish.txt","rt")
cc=oo.readlines()
for j in cc:
    a = str(j).replace("/", "     ")

    ww = open("kasaba_separated.txt", "a")
    ww.write(str(a))
    ww.close()

import os
os.system("sed -i '/^$/d' kasaba_separated.txt ")
os.system("awk '{print $1}' kasaba_separated.txt >survey_number.txt")
os.system("awk '{print $2}' kasaba_separated.txt >kool.txt")
col = open("kool.txt", "rt")
import csv

zz = col.readlines()

for k in zz:
    ni = open("col_hisa.txt", "a")
    if str(k) == "\n":
        ni.write("*"+"\n")

    else:
        print(k)
        ni.write(str(k))



import csv

import os
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time
# os.system("sed -i '/^$/d' kasaba_separated.txt ")

chromedriver = "/home/hemanth/Desktop/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.maximize_window()
driver.get("https://landrecords.karnataka.gov.in/service53/")

time.sleep(2)

driver.find_element_by_xpath("//*[@id='rdoSurvey']").click()

time.sleep(5)

district = driver.find_element_by_xpath('/html/body/form/div[5]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div[2]/div/select')
dropdistrict = Select(district)
dropdistrict.select_by_value("28")

time.sleep(6)

taluk = driver.find_element_by_xpath('/html/body/form/div[5]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div[4]/div/select')
droptaluk = Select(taluk)
droptaluk.select_by_value("1")

time.sleep(4)

hobli = driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[2]/div[6]/div/select")
drophobli = Select(hobli)
drophobli.select_by_value("1")

time.sleep(6)

kvl = open("village_loop.txt", "rt")
vl=csv.reader(kvl)


khl = open("col_hisa.txt", "rt")
el = csv.reader(khl)



survey_No = open("survey_number.txt", "rt")
sn = csv.reader(survey_No)


for vv,vl,el in zip(vl,sn,el):
    village= driver.find_element_by_xpath('//*[@id="ddl_Village"]')
    dropvillage= Select(village)
    dropvillage.select_by_visible_text(vv[0])
    print(vv[0])
    time.sleep(6)

    se1 = driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[4]/div[2]/div/input")

    se1.clear()

    time.sleep(4)
    se = driver.find_element_by_xpath("/html/body/form/div[5]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[4]/div[2]/div/input")

    se.send_keys(vl[0])
    print(str(vl[0]))
    time.sleep(4)
    time.sleep(3)

    driver.find_element_by_xpath('//*[@id="Button1"]').click()

    time.sleep(10)

    star = driver.find_element_by_xpath('/html/body/form/div[5]/div/div/div[1]/div/div/div[1]/div[2]/div/div/div[1]/div[2]/div[1]/div[4]/div[5]/div/select')
    dropstar = Select(star)
    dropstar.select_by_visible_text("*")
    print("*")


    time.sleep(10)
    try:
     fb1 = driver.find_element_by_xpath('//*[@id="ddl_hissa"]')
     bu = Select(fb1)
     bu.select_by_visible_text(el[0])
     print(el[0])
     time.sleep(10)

    except:
         continue

    parent = driver.current_window_handle
    driver.find_element_by_xpath('//*[@id="btnFetchDetails"]').click()

    time.sleep(10)
    child = driver.window_handles
    for c in child:
        if c != parent:
            driver.switch_to.window(c)

            time.sleep(4)

            table1 = driver.find_element_by_xpath('//*[@id="ownerdetails"]/table')
            table2 = driver.find_element_by_xpath('//*[@id="landdetails"]/table')
            table3 = driver.find_element_by_xpath('//*[@id="land"]/table')
            print(table1.text)
            print(table2.text)
            print(table3.text)

            tt1 = table1.text
            tt2 = table2.text
            tt3 = table3.text

            zx = open(str(vv) + str(vl) + str(el) + ".txt", "a")

            zx.write(str(tt1) + "\n")
            zx.write(str(tt2) + "\n")
            zx.write(str(tt3) + "\n")
            time.sleep(5)


            driver.close()
    driver.switch_to.window(parent)









