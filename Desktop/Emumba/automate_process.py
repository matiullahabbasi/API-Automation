
import paramiko
import scp
import getpass

# Variables
local_file = r'C:\Users\Emumba\Desktop\Emumba\Assignment_Part_A_environment.json'
install_script = r'C:\Users\Emumba\Desktop\Emumba\install_libraries.py'
remote_host = '192.168.0.70'
remote_user = 'emumba'
remote_dir = 'C:/Users/Emumba/Desktop/newfolder/'

# Prompt for password
password = getpass.getpass(prompt='Enter your SSH password: ')

# Create SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh.connect(remote_host, username=remote_user, password=password)
    print("Connection successful!")

    # Upload files using SCP
    with scp.SCPClient(ssh.get_transport()) as scp_client:
        scp_client.put(local_file, remote_path=remote_dir + 'Assignment_Part_A_environment.json')
        scp_client.put(install_script, remote_path=remote_dir + 'install_libraries.py')

    # Execute the installation script
    stdin, stdout, stderr = ssh.exec_command(f'python {remote_dir}install_libraries.py')

except paramiko.AuthenticationException:
    print("Authentication failed. Please check your credentials.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    ssh.close()
