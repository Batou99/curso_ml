import urllib
import urllib.request
# If you are using Python 3+, import urllib instead of urllib2

import json 

data =  {

    "Inputs": {

        "input1":
        {
            "ColumnNames": ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"],
            "Values": [ [ "0", "0", "0", "0", "value" ], [ "0", "0", "0", "0", "value" ], ]
        },        },
    "GlobalParameters": {
    }
}

body = str.encode(json.dumps(data))

url = 'https://ussouthcentral.services.azureml.net/workspaces/c367577cb80e4f1cb797ea846c288863/services/d0ce8d614bfb45a787d3df332854730d/execute?api-version=2.0&details=true'
api_key = 'UpqO3GCnyOdJzDKFuqFuCxd56qL15ZJBpCF053oe7SByxT1OpCaMN1010EMLX5727hiTLonFW7x5zd8eP80TBg==' # Replace this with the API key for the web service
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers) 

try:
    response = urllib.request.urlopen(req)

    # If you are using Python 3+, replace urllib2 with urllib.request in the above code:
    # req = urllib.request.Request(url, body, headers) 
    # response = urllib.request.urlopen(req)

    result = response.read()
    print(result) 
except urllib.request.HTTPError:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())

    print(json.loads(error.read()))
