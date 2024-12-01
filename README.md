# Backdoor-Python

A Python program that sets up a TCP Server that listens for client connections, allowing the server to be able to gain access to the client and run various commands. The commands including viewing and modification of directories, transferring files, deleting files, or complete takeover of all inputs.

**Important**: This program is an extremely powerful and dangerous program to use. It can potentially lead to destructive and illegal activities. This project is only to be used for education purposes. I do not hold any liability if used maliciously. Please do not use this for harm or illegal activities.


# Documentation

**Libraries Used**

1. **os**: A library that allows the user to interact with the operating system more seemlessly
2. **socket**: Sets up TCP connections between two or multiple computers allowing for information exchange
3. **sys**: Provides access to variables and functions which can influence the interpreter
4. **time**: Provides functions to work with time-related operations

**Commands**

1. **view_cwd**

**Purpose**: Returns current working directory of where the file is on the client computer

**Operation**: Sends the _view_cwd_ command, receives all files in current working directory and outputs


2. **custom_dir**

**Purpose**: Return a server requested directory listing

**Operation**: Prompts the server to type a directory or file, sends path to client, and outputs results


3. **download_file**

**Purpose**: Download a specific file or diretory from the client to the server

**Operation**: Sends the _download_file_ command after server types a path in the prompt, file is transfered in binary mode and saved


4. **delete_file**

**Purpose**: Delete a server requested file or directory on client system

**Operation**: Sends the _delete_file_ command after server types a path in the prompt, with confirmation message on success


5. **send_file**

**Purpose**: Send a server selected file to client's system

**Operation**: Sends _send_file_ command along with a path to served selected file, file transfered in binary mode and saved on client system.


6. **open_file**

**Purpose**: Force open directory or file on client system

**Operation**: Sends _open_file_ command along with a file path, forcefully opening file on client's system


7. **lock_all**

**Purpose**: Lock client system keyboard and mouse

**Operation**: Sends the _lock_all_ command, triggering mouse and keyboard to become unresponsive and switching lock_engaged to _True_


8. **unlock_all**

**Purpose**: Unlock client system keyboard and mouse

**Operation**: Sends the _unlock_all_ command, triggering mouse and keyboard to become responsive again and switching lock_engaged to _False_


9. **delete_all_files**

**Purpose**: Delete all files on the client's system

**Operation**: Sends the _delete_all_files_ command, client system attempts to delete all files, even the script itself.

10. **self-destruct** (Still in Testing)

**Purpose**: Shut down client's system

**Operation**: Sends the _self_destruct_ command, a command executes to shutdown the computer, server cuts connection.



# Security and Ethical Guidelines

1. **Consent**: Ensure that you have consent of the client to use this software to connect to their system before setting up a connection between your and their system. Do not use this without consent.

2. **Destructive Commands**: Be aware of the destruction that a few of the commands can do like **delete_all_files**, **delete_file**, as those damages are irreversible and can not be restored.

3. **Network Security**: Use this program in a secure and trusted environment. The reason is to prevent any senstive data that is being transferred between the server and client is not read by anyone. The data transfer is not encrypted. That could be a project you could do however.



Enjoy!
