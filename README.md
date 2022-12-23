# MQTT-Implementation-with-dokcer-swarm
Hi,
This Project demonstrates how can we use the docker swarm to create 3 services:
 1) Broker --> which acts kind of a server, recieves and deliver messages with a specific topic 
 2) Subscriber --> Subscribes a topic and recieve messages on that. 
 3) Publisher --> Publishes the messages onto a specific topic.
 
 
 I'm using Docker Swarm to create a cluster whcih these three services running in a specific network. Network type is overlay with fix IP Range.
