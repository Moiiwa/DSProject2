from typing import List
import requests
import os.path
class Client:

    target_host = None

    address = None


    def listen_for_commands(self):
        command = "continue"
        while (command != "stop"):
            command = input()
            command_els = command.split(' ')
            command_type = command_els[0]
            self.address = "http://"+self.target_host + ":1337/" + command_type + "/"

            if self.target_host != None:
                if command_type == "init":
                    self.process_init(command_els)
                elif command_type == "create":
                    self.process_create(command_els)
                elif command_type == "read":
                    self.process_read(command_els)
                elif command_type == "write":
                    self.process_write(command_els)
                elif command_type == "delete":
                    self.process_delete(command_els)
                elif command_type == "info":
                    self.process_info(command_els)
                elif command_type == "copy":
                    self.process_copy(command_els)
                elif command_type == "move":
                    self.process_move(command_els)
                elif command_type == "open_dir":
                    self.process_open_dir(command_els)
                elif command_type == "read_dir":
                    self.process_read_dir(command_els)
                elif command_type == "make_dir":
                    self.process_make_dir(command_els)
                elif command_type == "delete_dir":
                    self.process_delete_dir(command_els)
                elif command_type == "help":
                    self.process_help()
                elif command_type == "inithost":
                    self.process_initialize_name_server(command_els)
                elif command_type != "stop":
                    print("!!!Unknown command, use \'help\' to see the list of commands")
            elif command_type != "inithost":
                print("You need to use \'inithost\' command first to initialize nameserver")
            else:
                self.process_initialize_name_server(command_els)


    def process_help(self):
        print("We use the following commands:\n")
        print("inithost <name of name server> - initializes name server ")
        print("init - Initialize the storage, removes any existing files in root directory and returns available size\n")
        print("create <name of file> - creates new empty file with a given name\n")
        print("read <name of file> - downloads file from server and prints its content\n")
        print("write <name of file> - reads a file and sends it to the storage\n")
        print("delete <name of file> - deletes file\n")
        print("info <name of file> - provides information about the file\n")
        print("copy <name of file> - copies file\n")
        print("move <name of file> <target path> - moves file to the target path\n")
        print("open_dir <directory name> - changes directory\n")
        print("read_dir <directory name> - prints the contents of the directory\n")
        print("make_dir <directory name> - creates new directory\n")
        print("delete_dir <directory_name> - removes directory")


    def process_init(self, command_elements: List):
        if len(command_elements) == 1:
            response = requests.post(self.address)
            if response.status_code == 200:
                print("Client is initialized")
        else:
            print("Incorrect number of arguments, use \'help\' to check the correct one")


    def process_create(self, command_elements: List):
        if len(command_elements) == 2:
            parameters = {'filename': command_elements[1]}
            response = requests.post(self.address, params=parameters )
            if response.status_code == 200:
                print("File is created")
        else:
            print("Incorrect number of arguments, use \'help\' to check the correct one")


    def process_read(self, command_elements: List):
        if len(command_elements) == 2:
            parameters = {'filename': command_elements[1]}
            response = requests.get(self.address, params=parameters)
            if response.status_code == 200:
                with open('file', 'wb') as f:
                    f.write(response.content)
                print("File is read")
        else:
            print("Incorrect number of arguments, use \'help\' to check the correct one")


    def process_write(self, command_elements: List):
        if len(command_elements) == 2:
            file = open(command_elements[1], 'r')
            content = file.read()
            parameters = {'filename': command_elements[1], 'content': content}
            response = requests.post(self.address, params=parameters )
            if response.status_code == 200:
                print("File is written")
        else:
            print("Incorrect number of arguments, use \'help\' to check the correct one")


    def process_delete(self, command_elements: List):
        if len(command_elements) == 2:
            parameters = {'filename': command_elements[1]}
            response = requests.post(self.address, params=parameters)
            if response.status_code == 200:
                print("File was deleted")
        else:
            print("Incorrect number of arguments, use \'help\' to check the correct one")


    def process_info(self, command_elements: List):
        if len(command_elements) == 2:
            parameters = {'filename': command_elements[1]}
            response = requests.get(self.address, params=parameters)
            if response.status_code == 200:
                print(response.content)
        else:
            print("Incorrect number of arguments, use \'help\' to check the correct one")


    def process_copy(self, command_elements: List):
        if len(command_elements) == 2:
            parameters = {'filename': command_elements[1]}
            response = requests.post(self.address, params=parameters)
            if response.status_code == 200:
                print("File was copied")
        else:
            print("Incorrect number of arguments, use \'help\' to check the correct one")


    def process_move(self, command_elements: List):
        if len(command_elements) == 3:
            parameters = {'filename': command_elements[1], 'target_dir': command_elements[2]}
            response = requests.post(self.address, params=parameters)
            if response.status_code == 200:
                print("File was moved")
        else:
            print("Incorrect number of arguments, use \'help\' to check the correct one")


    def process_open_dir(self, command_elements: List):
        if len(command_elements) == 2:
            parameters = {'directory': command_elements[1]}
            response = requests.post(self.address, params=parameters)
            if response.status_code == 200:
                print("Directory changed")
        else:
            print("Incorrect number of arguments, use \'help\' to check the correct one")


    def process_read_dir(self, command_elements: List):
        if len(command_elements) == 2:
            parameters = {'directory_name': command_elements[1]}
            response = requests.get(self.address, params=parameters)
            if response.status_code == 200:
                print(response.content)
        else:
            print("Incorrect number of arguments, use \'help\' to check the correct one")


    def process_make_dir(self, command_elements: List):
        if len(command_elements) == 2:
            parameters = {'directory_name': command_elements[1]}
            response = requests.post(self.address, params=parameters)
            if response.status_code == 200:
                print("Directory created")
        else:
            print("Incorrect number of arguments, use \'help\' to check the correct one")


    def process_delete_dir(self, command_elements: List):
        if len(command_elements) == 2:
            parameters = {'directory_name': command_elements[1]}
            response = requests.post(self.address, params=parameters)
            if response.status_code == 200:
                print("Directory deleted")
        else:
            print("Incorrect number of arguments, use \'help\' to check the correct one")


    def process_initialize_name_server(self, command_elements: List):
        if len(command_elements) == 2:
            f = open('setting.txt','w')
            f.write(command_elements[1])
            self.initialize_name_server()
        else:
            print("Incorrect number of arguments, use \'help\' to check the correct one")


    def initialize_name_server(self):
        f = open("setting.txt","r")
        self.target_host = f.read()


if __name__ == '__main__':
    client = Client()
    if os.path.isfile('setting.txt'):
       client.initialize_name_server()
    else:
       print("You need to use \'inithost\' command to initialize nameserver")
    client.listen_for_commands()

