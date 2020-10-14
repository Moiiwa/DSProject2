# DSProject2

<b>How it works</b>

How does our project Ideally should work.

User writes command to the command line using one of the commands which are:

inithost <name of name server> - initializes name server 

init - Initialize the storage, removes any existing files in root directory and returns available size

create *name of file* - creates new empty file with a given name

read *name of file* - downloads file from server and prints its content

write *name of file* - reads a file and sends it to the storage

delete *name of file* - deletes file

info *name of file* - provides information about the file

copy *name of file* *target path* - copies file

move *name of file* *target path* - moves file to the target path

open_dir *directory name* - changes directory

read_dir *directory name* - prints the contents of the directory

make_dir *directory name* - creates new directory

delete_dir *directory name* - removes directory

This list is accessible with *host* command. 
Other actions, but inithost are unavailable till we don't initialize namenode with inithost.

Then request goes to the namenode, which checks the availability of storage servers,
and sends request either to do something with directory/file or to get it.

Availability of storages is checked before each operation, when storage
falls down it is added to the list of fallen storages, and when next check will happen, it 
will check if storage became available, if yes, new data is writtern into it
and it becomes available to fetch data from it.

To add new storage server get request with host ip should be sent to the namenode.
So basically, we have thin client, most of the load goes to namenode, and storages just do the basic work they have to.
Names repetitions are also considered while storing new file/directory.

<b>How to run</b>

Our project has problems with running in docker, you can use storage server image,
but we recommend to use scripts of namenode and clients as they are. Run servers in docker,
start namenode script and send host and port of storage to *hostip*:1337/init_serv/.
Then run client and initialize namenode with command inithost *host_ip*.

<b>Contribution:</b>
Fronts Daniil - storage server,
Tikhonov Nikita - namenode,
Gudkov Mikhail - client (and docker :( )