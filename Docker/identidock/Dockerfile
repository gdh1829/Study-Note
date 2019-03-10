# uses python3 latest image
FROM python:3

# [IMPORTANT] To prevent the containter run by root as same as host root and protect host security, you have to create another UID and GID.
# Without this line, it would turn out that processes in container are being run by root, which is as same as host root. 
# Then your host UID and GID will be exposed to hackers, if a hacker hacked your container, they would be able to hack your host too.
# Because Linux Kernel confirms users and decides the access permission by using UID and GID. OS is mapping Identifier with UID and GID in userspace.
# So even though UIDs in container are same as the ones in host, the users and groups created in container do not affect host.
# In this case, it could be confusing with access permission. Files could be seen like they have different ownerships in and outside of container. 
# So it is very significant to always set USER in Dockerfile or to change users by using ENTRYPOINT or CMD script.
RUN groupadd -r uwsgi && useradd -r -g uwsgi uwsgi
# installs Flask - ligthweight Python WebFramework
RUN pip install Flask uWSGI requests redis
# work directory
WORKDIR /usr/src/app
# copy host source file to /usr/src/app in docker container
COPY app /usr/src/app
# script to optionally execute dev and prod environment
COPY cmd.sh /
# makes other containers also able to access to this container as well as host
EXPOSE 9090 9191
# Sets up uWSGI user who is going to execute the commands after this line including CMD and ENTRYPOINT
USER uwsgi

# command 
# CMD ["python", "identidock.py"]
CMD ["/cmd.sh"]
