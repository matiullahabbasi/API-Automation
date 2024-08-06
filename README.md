# API-Automation
1. **Initial Setup:**
   - Created an installation script to set up the environment on the remote server, including installing necessary libraries, Node.js, Newman, etc.
2. **Manual Process:**
   - Uploaded the installation script to the remote server using the SCP command.
   - Executed the script manually on the remote server to set up the environment.
3. **Automation Attempt:**
   - Developed a Python script to automate the entire process:
     a) Configured SSH authentication using a username and password.
     b) Automated the transfer of files from the local machine to the remote server.
     c) Executed the installation script remotely to install the required libraries and tools.