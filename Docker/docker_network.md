Docker Networking
===

## Network drivers
 * `bridge`  
    The default network driver.  
    Usally used when your applications run in standalone containers that need to communicate.  
    __User-defined bridge networks are best when you need multiple containers to communicate on the same Docker host.__  
 * `host`  
    For standalone containers, remove network isolation between the container and the Docker host, and use the host's networking directly.  
    Only available for swarm services on Docker 17.06 and higer.  
    __Host networks are best when the network stack should not be isolated from the Dockerhost, but you want other aspects of the container to be isolated.__
 * `overlay`  
    Connect multiple Docker Daemons together and enable swarm services to communicate with each other.  
    You can also use overlay networks to facilitate communication between a swarm service and a standalone container, or between two standalone containers on different Docker daemons.  
    This strategy removes the need to do OS-level routing between these containers.
    __Overlay networks are best when you need containers running on different Docker hosts to communicate, or when multiple applications work together using swarm services.__  
 * `macvlan`  
    Allow you to assign a MAC address to a container, making it appears as a physical device on you network. The docker daemon routes traffic to containers by their MAC addresses. 
    Using the `macvlan` driver is sometimes the best choice when dealing with legacy applications that expect to be directly connected to the physical network, rather than routed through the Docker host's network stack.  
    __Macvlan networks are best when you are migrating from a VM setup or need your containers to look like physical hosts on your network, each with a unique MAC address.__
 * `none`  
    For this container, disable all networking. Usually used in conjunction with a customer network driver.  
    Not available fr swarm services.  
 * __Network plugins__  
    You can install and use third-party network plugins with Docker. These plugins are avaiable from Docker Hub or from third-party vendors.
    __Third-party network plugins allow you to integrate Docker With specialized network stacks.__

## Use user-defined bridge networks
```bash
# docker network list
$ docker network ls 

# create a new brdige type network named after alpine-net
# --driver bridge: You don't need this flag since it's default.
$ docker network create --driver bridge alpine-net 

# checkout the newly created network
$ docker network inspect alpine-net

# connect docker containers to the specific network that we've created before
docker run -dit alpine1 --network alpine-net alpine ash
docker run -dit alpine2 --network alpine-net alpine ash
docker run -dit alpine4 --network alpine-net alpine ash

# let the container connected to default network, bridge
docker run -dit alpine3 alpine ash

# During the docker run command, you can attach only single network.
# Then, if you'd like more networks, use the docker network connect command
# docker network connect <network name> <target conatainer>
docker network connect bridge alpine4

# Let's check out each of networks which containers they have 
docker network inspect bridge | jq .[0].Containers
docker network inspect alpine-net | jq .[0].Containers
```

On user-defined networks like `alpine-net`, containers can not only communicate by IP address, but can also resolve a container name to an IP address. This capability is called __automatic service discovery__.  

From alpine1, you should not be able to connect to alpine3 at all, since it is not on the alpine-net network.  

Not only that, but you can't connect to alpine3 from alpine1 by its IP address either. Look back at the `docker network inspect` output for the `bridge` network and find `alpine3`'s IP address  

```ash
/ # ping -c 2 alphine3
ping: bad address 'alphine3'

/ # ping -c 2 172.17.0.2
PING 172.17.0.2 (172.17.0.2): 56 data bytes

--- 172.17.0.2 ping statistics ---
2 packets transmitted, 0 packets received, 100% packet loss
```

Remember that alpine4 is connected to both the default `bridge` network and `alpine-net`. It should be able to reach all of the other containers. However, you will need to address `alpine3` by its IP address.

```ash
$ docker container attach alphine4
/ # ping -c 2 alpine1
ping: bad address 'alpine1'

/ # ping -c 2 172.17.0.4
PING 172.17.0.4 (172.17.0.4): 56 data bytes
64 bytes from 172.17.0.4: seq=0 ttl=64 time=0.214 ms
64 bytes from 172.17.0.4: seq=1 ttl=64 time=0.223 ms

--- 172.17.0.4 ping statistics ---
2 packets transmitted, 2 packets received, 0% packet loss
round-trip min/avg/max = 0.214/0.218/0.223 ms
```

As a final test, make sure your containers can all connect to the internet by pinging `google.com`. You are already attached to `alpine4` so start by trying from there. Next, detach from `alpine4` and connect to `alpine3` (which is only attached to the `bridge` network) and try again. Finally, connect to `alpine1` (which is only connected to the `alpine-net` network) and try again.