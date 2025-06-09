# **Structure** 

- **Inventory folder**: The inventory Folder the list of servers (hosts) that Ansible will manage.
  - **Hosts**: Hosts are the systems that Ansible will manage. The hosts can be specified in an inventory file, which is a plain text file that lists the hostnames or IP addresses of the systems that Ansible should manage.
- **Roles and Tasks**: Roles are a way to organize playbooks and other files in a structured way. A role represents a specific function or a set of tasks, such as installing a specific software package or configuring a service.Define specific tasks to be executed on the remote server(s).
  - **Tasks** are the individual actions that Ansible will perform on the hosts. Tasks are defined in playbooks, which are written in YAML and specify the order in which tasks should be executed.
- **Playbook**: The main file that ties together the inventory, roles, tasks, and remote user details to orchestrate automation.

## **Inventory File**

- **Definition**: A file (typically named `hosts`) in the `inventory` directory that lists the remote servers Ansible will connect to.
- **Details**:
  - Contains IP addresses or domain names of remote machines.
  - Example: A single IP address for one remote server, but multiple servers can be listed.
  - Path: `inventory/hosts`.
  - Example content:
    ```
    [gcp_host]
    <IP_ADDRESS> ansible_user=rahul ansible_ssh_private_key_file=<path_to_private_key>
    ```
  - **Purpose**: Tells Ansible which servers to target for automation tasks.

## **Roles and Tasks**

- **Definition**: Roles are a way to organize tasks in Ansible. Each role contains tasks defined in a `main.yml` file.
- **Structure**:
  - Path: `roles/<role_name>/tasks/main.yml`.
  - Example Role: `python`.
  - Tasks in `main.yml` for example
    1. Install Python.
    2. Create a directory (e.g., `basic_http_server`).
    3. Install Apache web server.
- **Purpose**: Roles modularize tasks, making the project reusable and organized.

## **Ansible Playbook**

- **Definition**: The main YAML file (e.g., `vmsetup_playbook.yml`) that defines the automation workflow.
- **Components**:
  - **Name**: A descriptive name for the playbook (e.g., "VM Setup Playbook").
  - **Hosts**: Specifies which hosts from the inventory file to target (e.g., `hosts: all` to target all servers in the inventory).
  - **Remote User**: The username used to connect to the remote server via SSH (e.g., `remote_user: ubuntu` ).
  - **Roles**: Specifies the roles to execute (e.g., `roles: `).
- **Example Playbook** (`vmsetup_playbook.yml`):
  ```yaml
  - name: VM Setup Playbook
    hosts: all
    remote_user: michael
    roles:
      - python
  ```
- **Purpose**: Orchestrates the execution of tasks on specified hosts.

## **Executing the Ansible Playbook**

- **Command**:

  ```bash
  ansible-playbook -i inventory/hosts main_palybook.yml
  ```

  - **Breakdown**:
    - `ansible-playbook`: The command to run the playbook.
    - `-i inventory/hosts`: Specifies the path to the inventory file.
    - `main_palybook.yml`: The playbook file to execute.
- **Authentication**:

  - Uses SSH with a private key (no password needed) or username/password.
  - Example SSH command for verification:
    ```bash
    ssh -i <private_key> michael@<IP_ADDRESS>
    ```
- **Execution Process**:

  - Ansible connects to the remote server(s) listed in the inventory.
  - Executes tasks defined in the role (e.g., install Python, create a directory, install Apache).
  - Outputs the status (e.g., `changed=3` for three successful tasks).

## **Key Notes**

- **Host File Flexibility**: Can include multiple servers for scalability.
- **Remote User**: Must match the user on the remote server (e.g., `root`).
- **SSH Authentication**:

  - Private/public key pair is recommended for secure, passwordless access.
  - Username/password can be used if keys are not configured.
