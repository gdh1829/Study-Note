Bind Mount
===

You have source codes in your host.  
You would like to create Docker containter with the source codes that you have.  

Then, you can prepare Dockerfile and build the image
> docker build -t MyApp .

Then, you can run the image that you have created.
> docker run -d -p 5000:5000 MyApp

But there is something that makes you pissed off. 
Every time you change your source codes, you should rebuild your image and restart the container.  
What a frustrating!  

So, `Bind Mount` let you get away from the problem.  
We can __bind mount__ the host's source code folder on the one in the container! - `-v HOST_DIR:CONTAINTER_DIR`  
Your code changes are instantly applied to the container's.  
> docker run -d -p 5000:5000 -v "$(pwd)"/app:/usr/src/app MyApp    

※In Docke, `HOST` always instructs the machine running Docker Engine. If you are using remote Docker Daemon, the path must be existed in the remote machine. If you are using docker machine in virtual machine, it is recommended to cross mount home directory for development convenience.

`-v "$(pwd)"/app:/usr/src/app MyApp` lets app directory mounted on /app directory in the container. Thanks to it, you can override /app directory of the container in host, at the same time can write it in the containter. If you don't want, you can also mount the volume with read-only.

The path for -v argument must be absolute path.

※Before you do the bind mount, you need to delete the previous images
> docker stop $(docker ps -lq)  
> docker rum $(docker ps -lq)  
docker ps -lq returns the latest used containter id.