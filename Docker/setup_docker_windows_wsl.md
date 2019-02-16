How to set up Docker for Windows and WSL
===
[Reference Here](https://nickjanetakis.com/blog/setting-up-docker-for-windows-and-wsl-to-work-flawlessly)

1. download [docker for windows](https://docs.docker.com/docker-for-windows/install/)

2. install with default setting

3. configure docker for windows, after the install is done.
    1. open docker Settings
    2. move to General tab
    3. check check-box for `Expose daemon on tcp://localhost:2357 without TLS`  
      It helps legacy clients connect to the daemon. It also makes yourself vulunerable to remote code execution attacks. use with caution.  
      Because any time you make a network connection that is not encrypted, it is worth talking about but in this case it is completely safe because we are never connecting to it over a public network.  
      This is going to allow your local WSL instance to connect locally to the Docker daemon running within Docker for Windows. The traffic is not even leaving your dev box since the daemon is only bound to _localhost_, so not even other machines on your local network will be able to connect. In other words, it's very safe for this data to be transmit over plain text.  
    4. move to Shared Drives tab
    5. select the local drives you want to be available to your containter.
        You may also want to share any drives you plan on having your source code reside on. This step is not necessary but I keep my code on an internal secondary HD.
4. install Docker and Docker Compose within WSL
    - The following instructions are for Ubuntu 18.04, but if you happen to use a different WSL distribution, you can follow Docker's installation guide for your distro from [Docker's installation docs](https://docs.docker.com/install/#supported-platforms)
    - Here is the Ubuntu 18.04 installation notes taken from Docker's documentation
```Bash
# Update the apt package list with y decision
sudo apt-get update -y

# Install Docker's package dependencies
sudo apt-get install -y \
     apt-transport-https \
     ca-certifiactes \
     curl \
     gnupg-agent \
     software-properties-common

# Download and add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Verify the fingerprint
sudo apt-get fingerprint 0EBFCD88

# Add the 'stable' cahnnel's Docker upstream repository
sudo add-apt-repository \
     "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
     $(lsb_release -cs) \
     stable"

# Update the apt package list (for the enw apt repo).
sudo apt-get update -y

# Install the latest version of Docker CE
#
# At this point, it is a little different from Docker's Offical Docs
# You just only need docker-ce not docker-ce-cli and containerd.io
# Because you have already installed docker things like docker-ce-cli on Windows and you just need to connect wsl docker-ce to Windows Docker.  
sudo apt-get install -y docker-ce

# Allow your user to access the Docker CLI without needing root access
sudo usermod -aG docker $USER

# After all is done, you must close your terminal and open a new one so that you can run Docker without sudo.
```

5. Install Docker Compose  
    - We are going to install Docker Compose using PIP instead of the pre-compiled binary on GitHub because it runs a little bit faster (both are still Python apps).
```Bash
# Install Python and PIP
sudo apt-get install -y python python-pip

# Install Docker Compose into your user's home directory
pip install --user docker-compose
```

6. Configure WSL to Connect to Docker for Windows  
    - The next step is to configure WSL so that it knows how to connect to the remote Docker daemon running in Docker for Windows(remember, it's listening on port 2375).

    - Connect to a remote Docker daemon
```Bash
# This just adds the export line to your .bashrc file so it is available every time you open your terminal. The source commands reloads your bash configuration so you don't have to open a new terminal right now for it to take effect.
# In my case, despite the source command, I needed to reopen the new termina to take effect
echo "export DOCKER_HOST=tcp://localhost:2375" >> ~/.bashrc && source ~/.bashrc
```

7. Verify Everything Works
```Bash
# You should get a bunch of output about your Docker daemon
# If you get a permission denied error, close + open your terminal and try again.
docker info

# You should get back your Docker Compose version
docker-compose --version

# Verify that Docker CE is installed correctly by running the hello-world image
docker run hello-world
```

8. Ensure Volume Mounts Work  
    - The last thing we need to do is set things up so that volume mounts work.  
      When using WSL, Docker for Windows expects you to supply your volume paths in a format that matches this:`/c/Users/ko/dev/`  
      But, WSL doesn't work like that. Instead, it uses the `/mnt/c/Users/ko/dev` format. To get things to work for now, if you are running Windows 18.03(Spring 2018) or newer you can configure WSL to mount at `/` instead of `/mnt` .  

    - Running Windows 10 18.03+ or Newer
```Bash
# Open an new file
sudo nano /etc/wsl.conf

# Now make it look like this and save the file when you're done:
[automount]
root = /
options = "metadata"
```  
   - We need to set `root = /` because this will make your drives mounted at `/c` or `/e` instead of `/mnt/c` or `/mnt/e`. The `options = "metadata"` line is not necessary but it will fix folder and file permissions on WSL mounts so everything is not 777 all the time within the WSL mounts.  

9. Once you make those changes, reboot your computer.  