import subprocess

def install_libraries():
    # Install Chocolatey
    try:
        subprocess.run(["powershell", "-Command", "Start-Process", "powershell", "-ArgumentList", "'iex ((New-Object System.Net.WebClient).DownloadString(\"https://community.chocolatey.org/install.ps1\"))'", "-Verb", "RunAs"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing Chocolatey: {e}")

    # Install Node.js
    try:
        subprocess.run(["choco", "install", "nodejs", "-y"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing Node.js: {e}")

    # Install Newman
    try:
        subprocess.run(["C:\\Program Files\\nodejs\\npm.cmd", "install", "-g", "newman"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error installing Newman: {e}")

if __name__ == "__main__":
    install_libraries()
