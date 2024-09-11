sudo apt update
sudo apt update
sudo apt install xfce4 xfce4-goodies
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
sudo apt install ./chrome-remote-desktop_current_amd64.deb
sudo rm /workspaces/desktop/google-chrome-stable_current_amd64.deb
sudo rm /workspaces/desktop/chrome-remote-desktop_current_amd64.deb
sudo adduser aezteru --force-badname
sudo usermod -a -G chrome-remote-desktop aezteru
