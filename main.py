import json
import docker


client = docker.from_env()

#Get list of all services with data
servicelist = client.services()



#Get list of service ID

#for service in servicelist:
  #svcname = service['Spec']['Name']
  #svcreplica = service['Spec']['Mode']['Replicated']['Replicas']
  #svcid = service.id
  #svcdata = { "id": svcid,
   #           "name": svcname,
    #          "replica": svcreplica
    #        }
#print(json.dumps(svcdata, indent=2))


 #print("0 " + svcname + " replica=" + str(svcreplica))


for i in range(0,len(servicelist)-1):

 txt = json.dumps(servicelist[i])


 with open("dane.json", "w") as f:
    f.write(txt)

 f = open("dane.json")

 data = json.load(f)

 svcreplica = data["Spec"]["Mode"]["Replicated"]["Replicas"]
 svcname = data["Spec"]["Name"]
 print("0 " + svcname + " replica=" + str(svcreplica))
