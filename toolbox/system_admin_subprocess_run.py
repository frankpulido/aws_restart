# Author: Frank Pulido
# Date: June 10, 2025
# Purpose: SUBPROCESS Modul for admin tools using Python
# File: system_admin.py 
# Encoding: ASCII (a subset of UTF-8)
# Python 3.9.6

import subprocess

def run_command(command):
    """Runs a shell command and returns the output."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{command}': {e}")
        return None
    
def list_users():
    command = "dscl . -list /Users"
    return run_command(command)

def list_groups():
    command = "dscl . -list /Groups"
    return run_command(command)

def list_user_groups(username):
    command = f"dscl . -read /Users/{username} | grep 'GroupMembership'"
    return run_command(command)

def list_user_info(username):
    command = f"dscl . -read /Users/{username}"
    return run_command(command)

def list_group_members(groupname):
    command = f"dscl . -read /Groups/{groupname} | grep 'GroupMembership'"
    return run_command(command)

def create_user(username):
    command = f"sudo dscl . -create /Users/{username}"
    return run_command(command)

def delete_user(username):
    command = f"sudo dscl . -delete /Users/{username}"
    return run_command(command)

def create_group(groupname):
    command = f"sudo dscl . -create /Groups/{groupname}"
    return run_command(command)

def delete_group(groupname):
    command = f"sudo dscl . -delete /Groups/{groupname}"
    return run_command(command)

def add_user_to_group(username, groupname):
    command = f"sudo dscl . -append /Groups/{groupname} GroupMembership {username}"
    return run_command(command)

def remove_user_from_group(username, groupname):
    command = f"sudo dscl . -delete /Groups/{groupname} GroupMembership {username}"
    return run_command(command)

def install_package(package_name):
    command = f"sudo apt-get install -y {package_name}"
    return run_command(command)

def remove_package(package_name):
    command = f"sudo apt-get remove -y {package_name}"
    return run_command(command)

def update_system():
    command = "sudo apt-get update && sudo apt-get upgrade -y"
    return run_command(command)

def cleanup_system():
    command = "sudo apt-get autoremove -y && sudo apt-get autoclean"
    return run_command(command)

def update_environment_variables():
    command = "source /etc/environment"
    return run_command(command)
import subprocess

def clean_environment():
    """Cleans up environment variables."""
    try:
        command = "unset $(env | grep -E '^(PATH|LD_LIBRARY_PATH|PYTHONPATH)=' | cut -d= -f1)"
        return run_command(command)
    except Exception as e:
        print(f"Error cleaning environment: {e}")
        return None




def listing_files(directory):
    """Lists files in the specified directory."""
    command = f"ls -l {directory}"
    return run_command(command)

def get_system_info():
    """Returns system information including OS version, architecture, and hostname."""
    try:
        command = "uname -a"
        return run_command(command)
    except Exception as e:
        print(f"Error getting system info: {e}")
        return None

def get_active_processes():
    """Returns a list of active processes."""
    try:
        command = "ps aux"
        return run_command(command)
    except Exception as e:
        print(f"Error getting active processes: {e}")
        return None

def get_x_processes():
    """Returns a list of active processes with the 'x' option."""
    try:
        command = "ps -x"
        return run_command(command)
    except Exception as e:
        print(f"Error getting x processes: {e}")
        return None


print()
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])




def check_service_status(service_name):
    command = f"systemctl is-active {service_name}"
    status = run_command(command)
    if status == "active":
        return f"The service '{service_name}' is running."
    elif status == "inactive":
        return f"The service '{service_name}' is not running."
    else:
        return f"The service '{service_name}' status is unknown: {status}"
def start_service(service_name):
    command = f"sudo systemctl start {service_name}"
    return run_command(command)
def stop_service(service_name):
    command = f"sudo systemctl stop {service_name}"
    return run_command(command)
def restart_service(service_name):
    command = f"sudo systemctl restart {service_name}"
    return run_command(command)
def enable_service(service_name):
    command = f"sudo systemctl enable {service_name}"
    return run_command(command)
def disable_service(service_name):
    command = f"sudo systemctl disable {service_name}"
    return run_command(command)
def get_system_info():
    """Returns system information including OS version, architecture, and hostname."""
    try:
        os_info = subprocess.run("uname -a", shell=True, check=True, text=True, capture_output=True)
        return os_info.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error getting system info: {e}")
        return None