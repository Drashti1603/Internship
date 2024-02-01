import subprocess

def command(command):
    subprocess.run(command, shell=True)

def install():
    command('sudo apt update')
    command('sudo apt install openssh-server')

def start():
    command('sudo systemctl enable ssh')
    command('sudo systemctl start ssh')

def generate_ssh_key():
    command('ssh-keygen -t rsa')

def copy_ssh_key(remote_ip, username):
    command(f'ssh-copy-id {username}@{remote_ip}')

def test_connection(remote_ip, username):
    command(f'ssh {username}@{remote_ip} hostname')

def cp_dir(remote_ip, username, source_dir, destination_dir):
    command(f'scp -r {source_dir} {username}@{remote_ip}:{destination_dir}')
    

if __name__ == "__main__":
    install()
    start()

    remote_ip = input("IP address(remote machine): ")
    username = input("Remote username: ")

    generate_ssh_key()

    copy_ssh_key(remote_ip, username)
    test_connection(remote_ip, username)

    source_dir = input("Source directory: ")
    destination_dir = input("Destination directory(remote machine): ")

    cp_dir(remote_ip, username, source_dir, destination_dir)

