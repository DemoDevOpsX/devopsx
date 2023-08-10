import os
import json
from datetime import datetime
import requests
import datetime
import random

# import datetime,calendar
# date = datetime.datetime(2023, 1, 1, 0, 0)
# output = calendar.timegm(date.timetuple())

def send_metrics_data(application, co2value, dateepoch):
  
    token = os.getenv("UCV_API_TOKEN", "")
    ucvurl = "https://devopsx.watsonx.challenge:9443/api/v1/metrics"
    headers = {'Authorization': f'UserAccessKey {token}', 'accept': 'application/json', 'Content-Type': 'application/json' }
    params={
        "tenantId": "5ade13625558f2c6688d15ce",
        "dataSet": "week1",
        "record": {
            "metricDefinitionName": "CO2 Footprint",
            "recordName": "week1",
            "pluginType": "plugin",
            "dataFormat": "custom",
            "executionDate": dateepoch,
            "value": {"kg": co2value },
            "description": ""
        },
        "application": {"name": application}        
    }

    print(f"application={application} - co2val={co2value} - epoch={dateepoch}")
    print(f"data={json.dumps(params)}")
    r = requests.post(ucvurl, headers=headers, data=json.dumps(params), verify=False)
    response=json.loads(r.text)
    print(response)

    #      curl -X POST "https://devopsx.watsonx.challenge:9443/api/v1/metrics" \
    #   -H "accept: application/json" \
    #   -H "Authorization: UserAccessKey 7c5cc415-4807-46be-8646-8bc52454504f" \
    #   -H "Content-Type: application/json" \
    #   -k \
    #   -v \
    #   -d '{
    #         "tenantId": "5ade13625558f2c6688d15ce",
    #         "dataSet": "week1",
    #         "record": {
    #           "metricDefinitionName": "CO2 Footprint",
    #           "recordName": "Week1",
    #           "pluginType": "plugin",
    #           "dataFormat": "custom",
    #           "executionDate": 1688933713000,
    #           "value": {
    #             "kg": 18
    #           },
    #           "description": "Week1"
    #         },
    #         "application": {
    #           "name": "Emerald"
    #         }
    #       }'


def main():
    maxmonth=7
    print ("starting")
    datedic={
        "year": 2023,
        "month": random.randint(1, maxmonth),
        "day": random.randint(1, 28),
        "hour": random.randint(0, 23),
        "min":  random.randint(0, 59)
    }
    applications=["Emerald", "Inventory", "Accounting"]
    
    dt_obj=datetime.datetime(datedic["year"], datedic["month"], datedic["day"], datedic["hour"], datedic["min"])
    dateepoch = int(dt_obj.timestamp() * 1000)
    for application in applications:
        co2value=random.randint(0, 10)
        dateepoch = int(dt_obj.timestamp() * 1000)
        send_metrics_data(application, co2value, dateepoch)
if __name__ == '__main__':
    for _ in range(1, 10):
        # comment: 
        main()
    # end for
    
