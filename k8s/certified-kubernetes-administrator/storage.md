docker uses layered architecture
copy-on-write mechanism between image layers and container layers

/var/lib/docker
- volumes
- containers
- images
- aufs

volume mount vs bind mount
- volume mount mounts a volum from the volumes directory
- bind mount mounts a directory from any location on a docker host

who is responsible for this? It's the storage drivers!
- to maintain the layered architecture,
- creating writeable layer,
- moving files across layers to enable copy and write, etc

storage drivers
- aufs <- ubuntu default storage driver
- zfs
- btrfs
- device mapper
- overlay
- overlay2 
Docker는 OS에 따라 자동으로 가장 적합한 스토리지 드라이버를 선택. 각 드라이버는 특성과 퍼포먼스가 다름.

---
Volume은 Storage drivers가 핸들하는 것이 아닌, Volume drivers 플러그인이 핸들링.
- Local <- 디폴트 볼륨 드라이버 플러그인
- 그 외에도 많음. Azure File Storage, Convoy, DigitalOcean Block Storage, Flocker, gce-docker, GlusterFS, NetApp, RexRay, Portworx, VMware vSphere Storage, etc

Docker 컨테이너 기동시 volume driver를 선택할 수 있음.
- docker run -ti --name mysql --volume-driver rexray/ebs --mount src=ebs-vol,target=/var/lib/mysql mysql
  - aws cloud ebs를 사용한 볼륨 바인드 마운트 커맨드

---
Container Storage Interface(CSI)

---
Persistent Volume(PV)
- is a cluster-wide pool of storage volumes configured by an administrator to be used by users deploying applications on the cluster.
- The users can now select storage from this pool using Persistent Volume Claims(PVC).

---
Storage class
- static provisioning of volumes vs dynamic provisioning of volumes

kubectl get storageclass