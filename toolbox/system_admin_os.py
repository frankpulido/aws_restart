# Author: Frank Pulido
# Date: June 10, 2025
# Purpose: OS Modul for admin tools using Python
# File: system_admin.py 
# Encoding: ASCII (a subset of UTF-8)
# Python 3.9.6

import os

def new_user():
    confirm = 'N'
    while confirm.upper() != 'Y':
        username = input("Enter the new username: ").lower().strip()
        confirm = input(f"Confirm creation of user '{username}' (Y/N): ")
    try:
        os.system(f"sudo useradd {username}")
        print(f"User '{username}' created successfully.")
    except Exception as e:
        print(f"Error creating user '{username}': {e}")

def delete_user():
    confirm = 'N'
    while confirm.upper() != 'Y':
        username = input("Enter the username to delete: ").lower().strip()
        confirm = input(f"Confirm deletion of user '{username}' (Y/N): ")
    try:
        os.system(f"sudo userdel -r {username}")
        print(f"User '{username}' deleted successfully.")
    except Exception as e:
        print(f"Error deleting user '{username}': {e}")

def add_user_to_group():
    confirm = 'N'
    while confirm.upper() != 'Y':
        username = input("Enter the username to add to a group: ").lower().strip()
        print('These are the groups in the system:')
        list_groups()
        groupname = input("Enter the group name: ").lower().strip()
        confirm = input(f"Confirm adding user '{username}' to group '{groupname}' (Y/N): ")
    try:
        os.system(f"sudo usermod -aG {groupname} {username}")
        print(f"User '{username}' added to group '{groupname}' successfully.")
    except Exception as e:
        print(f"Error adding user '{username}' to group '{groupname}': {e}")

def remove_user_from_group():
    confirm = 'N'
    while confirm.upper() != 'Y':
        username = input("Enter the username to remove from a group: ").lower().strip()
        print('These are the groups in the system:')
        list_groups()
        groupname = input("Enter the group name: ").lower().strip()
        confirm = input(f"Confirm removing user '{username}' from group '{groupname}' (Y/N): ")
    try:
        os.system(f"sudo gpasswd -d {username} {groupname}")
        print(f"User '{username}' removed from group '{groupname}' successfully.")
    except Exception as e:
        print(f"Error removing user '{username}' from group '{groupname}': {e}")

def list_users():
    try:
        os.system("cut -d: -f1 /etc/passwd")
    except Exception as e:
        print(f"Error listing users: {e}")

def list_groups():
    try:
        os.system("cut -d: -f1 /etc/group")
    except Exception as e:
        print(f"Error listing groups: {e}")

def install_package():
    package_name = input("Enter the package name to install: ").lower().strip()
    try:
        os.system(f"sudo apt-get install {package_name}")
        print(f"Package '{package_name}' installed successfully.")
    except Exception as e:
        print(f"Error installing package '{package_name}': {e}")

def remove_package():
    package_name = input("Enter the package name to remove: ").lower().strip()
    try:
        os.system(f"sudo apt-get remove {package_name}")
        print(f"Package '{package_name}' removed successfully.")
    except Exception as e:
        print(f"Error removing package '{package_name}': {e}")

def update_system():
    try:
        os.system("sudo apt-get update && sudo apt-get upgrade -y")
        print("System updated successfully.")
    except Exception as e:
        print(f"Error updating system: {e}")

def cleanup():
    print("Cleaning up temporary files and caches...")
    try:
        os.system("sudo apt-get autoremove -y")
        os.system("sudo apt-get clean")
        print("Cleanup completed successfully.")
    except Exception as e:
        print(f"Error during cleanup: {e}")

def clean_environment():
    print("Cleaning up environment variables...")
    try:
        os.system("unset $(env | grep -E '^(PATH|LD_LIBRARY_PATH|PYTHONPATH)=' | cut -d= -f1)")
        print("Environment cleaned successfully.")
    except Exception as e:
        print(f"Error cleaning environment: {e}")

def update_environment():
    print("Updating environment variables...")
    try:
        os.system("sudo apt-get update")
        os.system("sudo apt-get upgrade")
        os.system("sudo apt-get dist-upgrade")
        print("Environment updated successfully.")
    except Exception as e:
        print(f"Error updating environment: {e}")

