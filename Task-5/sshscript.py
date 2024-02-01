import paramiko
import getpass

def establish_ssh_connection(hostname, username, password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(
            hostname=hostname,
            username=username,
            password=password,
            timeout=30  # Set the timeout here
        )
        print(f"SSH connection to {hostname} established successfully")
        return ssh_client

    except Exception as e:
        print(f"Error establishing SSH connection: {e}")
        return None

def copy_file(ssh_client, local_path, remote_path):
    try:
        with ssh_client.get_transport() as transport:
            scp = paramiko.SFTPClient.from_transport(transport)
            scp.put(local_path, remote_path)
            print(f"File {local_path} copied to {remote_path} successfully")

    except Exception as e:
        print(f"Error copying file: {e}")

if __name__ == "__main__":
    remote_host = input("hostname of the remote machine: ")
    remote_user = input("username for the remote machine: ")
    remote_pass = getpass.getpass("password for the remote machine: ")

    remote_ssh = establish_ssh_connection(remote_host, remote_user, remote_pass)

    if remote_ssh:
        local_file_path = input("local file path to copy: ")
        remote_file_path = input("the remote file path to copy to: ")

        copy_file(remote_ssh, local_file_path, remote_file_path)

        remote_ssh.close()
