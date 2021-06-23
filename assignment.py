import xml.etree.ElementTree as ET
from datetime import date
from datetime import timedelta
from datetime import datetime
import pytz
import json
import csv

#Question 1
def update_dep_ret(X: int, Y: int):
    tree = ET.parse('test_payload1.xml')
    root = tree.getroot()
    dep_new = date.today() + timedelta(days=X)
    ret_new = date.today() + timedelta(days=Y)
    root[0][2][0].text = dep_new.strftime("%Y%m%d")
    root[0][2][1].text = ret_new.strftime("%Y%m%d")
    tree.write("updated_test_payload1.xml")

#Question 2
def remove_json_elem(rem: str):
    with open('test_payload.json') as data_file:
        data = json.load(data_file)

    if rem in data:
        data.pop(rem, None)
    else:
        for elem in data:
            if rem in data[elem]:
                data[elem].pop(rem, None)
                break

    with open('updated_test_payload.json', 'w') as data_file:
        data = json.dump(data, data_file)


#Question 3
def response_parse(fName: str):
    with open(fName, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            r = dict(row)
            if int(r["responseCode"]) != 200:
                print("------------------")
                print("Label: " + r["label"])
                print("Response Code: " + r["responseCode"])
                print("Response Message: " + r["responseMessage"])
                print("Failure Message: " + r["failureMessage"])

                time = datetime.fromtimestamp(
                    int(r["timeStamp"])/1000, tz=pytz.timezone('US/Pacific'))
                print("Time: " + time.strftime("%Y-%m-%d %H:%M:%S"))


update_dep_ret(1, 5)
remove_json_elem("inParams")
response_parse("Jmeter_log1.jtl")
