#!/bin/bash
if [ -f /usr/bin/chromium ]; then    echo "Previous session running..." ; exit 0 ; fi

vnc_password=123456

mkdir ~/.cloudshell
touch ~/.cloudshell/no-apt-get-warning

sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get -yq install xfce4 xfce4-goodies vnc4server novnc websockify python-numpy chromium

printf "$vnc_password\n$vnc_password\n\n" | vncpasswd

echo "#!/bin/bash" > ~/.vnc/xstartup
echo 'xrdb /data/data/com.termux/files/home/.Xresources' >> ~/.vnc/xstartup
echo "startxfce4 &" >> ~/.vnc/xstartup

# Tweak resolution
vncserver -geometry 1920x1080

echo 'alias chromium="chromium --disable-dev-shm-usage"' > ~/.bashprofile
echo  "PS1='\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]$ '" >> ~/.bashprofile

if grep --quiet '. ~/.bashprofile'  ~/.bashrc; then
  echo ''
else
  echo '. ~/.bashprofile' >> ~/.bashrc
fi

sudo websockify -D --web=/usr/share/novnc/  8080 localhost:5901
