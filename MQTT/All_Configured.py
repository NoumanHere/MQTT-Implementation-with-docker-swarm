import docker
import subprocess
client = docker.from_env()

client.swarm.init()

node = client.nodes.list()
# node_id = str(node).replace("<",'').replace(">",'').replace("Node","").replace("[",'').replace("]",'').replace(":","").strip()
attr = node[0].attrs
Created_Date = attr['CreatedAt']
Name = attr['Description']['Hostname']
ID = attr['ID']


# # attr = node.attrs
# # Created_Date = attr['CreatedAt']
# # Name = attr['Description']['Hostname']
#subnet='20.30.40.2/24', gateway='20.30.40.1',iprange='20.30.40.2/4'


ipam_pool = docker.types.IPAMPool(subnet='10.10.10.2/24', gateway='10.10.10.1',iprange='10.10.10.2/24')
ipam_config = docker.types.IPAMConfig(pool_configs=[ipam_pool])
client.networks.create("test_network_1", driver = "overlay", scope = "global", attachable = True,ipam=ipam_config )


# #  Broker

subprocess.run(["docker","service","create","--name","broker","--replicas","3","--restart-condition","any","--network=test_network_1","--mount","type=bind,source=/home/nouman/Desktop/eclipse/mosquitto.conf,destination=/mosquitto/config/mosquitto.conf","eclipse-mosquitto:latest"]) 

# # ------------------>SERVICES<---------------------------------
# # SUB Service =  docker service create --network test_network_1  --replicas 3 efrecon/mqtt-client sub  -h 10.0.3.24  -p 1883  -t "Helloworld networks=['test_network_1']"

Pub = client.services.create("efrecon/mqtt-client",["sub","-h","10.10.10.4","-p","1883","-t","alfaisal_uni", "-v"],networks=['test_network_1'],name = "subscriber")
Pub.scale(replicas = 3)

# # PUB Service =  docker service create --network test_network_1 --replicas 3 efrecon/mqtt-client pub  -h 10.0.3.24  -p 1883  -t "Helloworld"  -m 'Test' -i "Nouman"
Sub = client.services.create("efrecon/mqtt-client",["pub","-h","10.10.10.4","-p","1883","-t","alfaisal_uni","-m","Name Here"],networks=['test_network_1'], name= "publisher")
Sub.scale(replicas = 3)

print("\n")
print("Swarm Details: \n")
print("Swarm Host Name: "+Name+", ID: "+ ID+", Created At: "+ Created_Date )

print("\n")
print("Publisher's ID, Name, Date of Creation")
pub = subprocess.call('./pub-info.sh')
print("\n")

print("Subscriber's ID, Name, Date of Creation")
sub = subprocess.call('./sub-info.sh')
print("\n")

subprocess.call('./test.sh')




This Project demonstrates how can we use the docker swarm to create 3 services:
1) Broker --> which acts kind of a server, recieves and deliver messages with a specific topic
2) Subscriber --> Subscribes a topic and recieve messages on that.
3) Publisher --> Publishes the messages onto a specific topic.


I'm using Docker Swarm to create a cluster whcih these three services running in a specific network. Network type is overlay with fix IP Range.
