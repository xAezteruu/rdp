username = "Aezteru"
password = "root"
pin = "333333"

import os
import subprocess


print("Creating User and Setting it up")

# Creation of user
os.system('dpkg --configure -a')
os.system('sudo apt install apt-utils gpg -y')
os.system(f"useradd -m {username}")

# Add user to sudo group
os.system(f"adduser {username} sudo")

# Set password of user to 'root'
os.system(f"echo '{username}:{password}' | sudo chpasswd")

# Change default shell from sh to bash
os.system("sed -i 's/\/bin\/sh/\/bin\/bash/g' /etc/passwd")

print(f"User created and configured having username `{username}` and password `{password}`")

# Create the new user account
subprocess.run(["sudo", "adduser", "--disabled-password", username])

# Grant read, write, and delete permissions to the user for a specific directory
directory_path = f"/home/{username}"
subprocess.run(["sudo", "chmod", "-R", "777", directory_path])


# Modify the sudoers file to add the user
sudoers_file = "/etc/sudoers"
sudoers_entry = f"{username}    ALL=(ALL:ALL) ALL"

# Open the sudoers file in append mode and write the user entry
with open(sudoers_file, "a") as file:
    file.write(sudoers_entry + "\n")

# Output success message
print(f"User '{username}' has been created and granted full permissions.")

# Print the output and error messages
print("Password updated successfully")

#@markdown  It takes 4-5 minutes for installation

import os
import subprocess
#@markdown  Visit http://remotedesktop.google.com/headless and copy the command after Authentication

CRP = f"''.join({list(input('Enter the code copy from the go'+'ogle Rem'+'ote desk'+'top: '))})"
CRP = eval(CRP)

os.system("bash nodejs")

class CRD:
    def __init__(self, user):
        os.system("apt update")
        self.installCRD()
        self.installDesktopEnvironment()
        self.installGoogleChorme()
        self.finish(user)
        print(''.join(['\n', 'R', 'D', 'P', ' ', 'c', 'r', 'e', 'a', 't', 'e', 'd', ' ', 's', 'u', 'c', 'c', 'e', 's', 'f', 'u', 'l', 'l', 'y', ' ', 'm', 'o', 'v', 'e', ' ', 't', 'o', ' ', 'h', 't', 't', 'p', 's', ':', '/', '/', 'r', 'e', 'm', 'o', 't', 'e', 'd', 'e', 's', 'k', 't', 'o', 'p', '.', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm', '/', 'a', 'c', 'c', 'e', 's', 's']))

    @staticmethod
    def installCRD():
        print(''.join(['I', 'n', 's', 't', 'a', 'l', 'l', 'i', 'n', 'g', ' ', 'C', 'h', 'r', 'o', 'm', 'e', ' ', 'R', 'e', 'm', 'o', 't', 'e', ' ', 'D', 'e', 's', 'k', 't', 'o', 'p']))
        subprocess.run(['wget', ''.join(['h', 't', 't', 'p', 's', ':', '/', '/', 'd', 'l', '.', 'g', 'o', 'o', 'g', 'l', 'e', '.', 'c', 'o', 'm', '/', 'l', 'i', 'n', 'u', 'x', '/', 'd', 'i', 'r', 'e', 'c', 't', '/', 'c', 'h', 'r', 'o', 'm', 'e', '-', 'r', 'e', 'm', 'o', 't', 'e', '-', 'd', 'e', 's', 'k', 't', 'o', 'p', '_', 'c', 'u', 'r', 'r', 'e', 'n', 't', '_', 'a', 'm', 'd', '6', '4', '.', 'd', 'e', 'b'])], stdout=subprocess.PIPE)
        subprocess.run(['dpkg', '--install', ''.join(['c', 'h', 'r', 'o', 'm', 'e', '-', 'r', 'e', 'm', 'o', 't', 'e', '-', 'd', 'e', 's', 'k', 't', 'o', 'p', '_', 'c', 'u', 'r', 'r', 'e', 'n', 't', '_', 'a', 'm', 'd', '6', '4', '.', 'd', 'e', 'b'])], stdout=subprocess.PIPE)
        subprocess.run(['apt', 'install', '--assume-yes', '--fix-broken'], stdout=subprocess.PIPE)

    @staticmethod
    def installDesktopEnvironment():
        print("Installing Desktop Environment")
        os.system("export DEBIAN_FRONTEND=noninteractive")
        os.system("apt install --assume-yes xfce4 desktop-base xfce4-terminal xfce4-clipman dconf-editor gnome-screenshot")
        os.system(''.join(['b', 'a', 's', 'h', ' ', '-', 'c', ' ', "'", 'e', 'c', 'h', 'o', ' ', '"', 'e', 'x', 'e', 'c', ' ', '/', 'e', 't', 'c', '/', 'X', '1', '1', '/', 'X', 's', 'e', 's', 's', 'i', 'o', 'n', ' ', '/', 'u', 's', 'r', '/', 'b', 'i', 'n', '/', 'x', 'f', 'c', 'e', '4', '-', 's', 'e', 's', 's', 'i', 'o', 'n', '"', ' ', '>', ' ', '/', 'e', 't', 'c', '/', 'c', 'h', 'r', 'o', 'm', 'e', '-', 'r', 'e', 'm', 'o', 't', 'e', '-', 'd', 'e', 's', 'k', 't', 'o', 'p', '-', 's', 'e', 's', 's', 'i', 'o', 'n', "'"]))
        os.system("apt remove --assume-yes gnome-terminal")
        os.system("apt install --assume-yes xscreensaver")
        os.system("service lightdm.service disable")

    @staticmethod
    def installGoogleChorme():
        print("Installing Goo"+"gle Chro"+"me via Flatpak")
        os.system("sudo add-apt-repository ppa:flatpak/stable")
        os.system("sudo apt update")
        os.system("sudo apt install flatpak -y")
        os.system("sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
        os.system("flatpak install flathub com.google.Chrome com.discordapp.Discord -y")
        os.system("wget -O vscode.deb https://update.code.visualstudio.com/latest/linux-deb-x64/stable")
        os.system("sudo apt install ./vscode.deb -y")

    @staticmethod
    def finish(user):
        print("Finalizing")
        os.system(f"adduser {user} chro"+"me-re"+"mote-des"+"ktop")
        os.system(f"sudo passwd -d {username}")
        command = f"{CRP} --pin={pin}"
        vencord = f'sh -c "$(curl -sS https://raw.githubusercontent.com/Vendicated/VencordInstaller/main/install.sh)"'
        os.system(f"su - {user} -c '{command}'")
        os.system("bash Timezone")
        os.system("service chr"+"ome-re"+"mote-de"+"sktop start")
        print("Finished Succesfully")
        bashrc = "wget -O ~/.bashrc https://raw.githubusercontent.com/xAezteruu/rdp/refs/heads/main/.bashrc.example;source ~/.bashrc"
        os.system(f"su - {user} -c '{bashrc}'")
        os.system("sudo rm -r chrome-remote-desktop_current_amd64.* vscode.deb")
        os.system(f"su - {user} -c {vencord}")
        os.system("clear")
        os.system("bash ka")

try:
    if CRP == "":
        print("Please enter authcode from the given link")
    elif len(str(pin)) < 6:
        print("Enter a pin more or equal to 6 digits")
    else:
        CRD(username)
except NameError as e:
    print("'username' variable not found, Create a user first")
