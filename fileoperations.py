# file handling in python is the ability to perform different operation on a file like reading from and writing to them.
#file operations in python are done using the built-in open() function. This function creates a file object, which would be utilized to call other support methods associated with it.
#syntax: file object = open(file_name [, access_mode][, buffering])
#file_name: The file_name argument is a string value that contains the name of the file that you want to access.
#access_mode: The access_mode determines the mode in which the file has to be opened, i.e., read, write, append, etc. A complete list of possible values is given below in the table. This is optional parameter and the default file access mode is read (r).
#buffering: If the buffering value is set to 0, no buffering takes place. If the buffering value is 1, line buffering is performed while accessing a file. If you specify the buffering value as an integer greater than 1, then buffering action is performed with the indicated buffer size. If negative, the buffer size is the system default(default behavior).
#The file object is like a cursor, which defines from where the data has to be read or written in the file. The file object can be used to call other support methods associated with it.
#There are various methods available with the file object. Some of them have been used in the following examples.
#Here is the list of complete set of File Methods.
#1	file.close()	Close the file. A closed file cannot be read or written any more
#2	file.flush()	Flush the internal buffer, like stdio's fflush. This may be a no-op on some file-like objects.
#3	file.fileno()	Return the integer file descriptor that is used by the underlying implementation to request I/O operations from the operating system.
#4	file.isatty()	Return True if the file is connected to a tty(-like) device, else False.
#5	file.next()	Return the next line from the file each time it is being called.
#6	file.read([size])	Read at most size bytes from the file. If the read hits EOF before obtaining size bytes, then it reads only available bytes. If the size argument is negative or omitted, read all data until EOF is reached
#7	file.readline([size])	Read one entire line from the file. A trailing newline character is kept in the string.
#8	file.readlines([sizehint])	Read until EOF using readline() and return a list containing the lines.

file = open("test.txt", "r")
print(file.read())
file.close()

data = open("test.txt", "r")
print(data.read())
data.close()

file = open("test.txt", "r")
file.write("This is the write command")
file.close()
file.flush()
file.isatty()

#file exceptional handling in python
#The try statement works as follows.
#First, the try clause (the statement(s) between the try and except keywords) is executed.
#If no exception occurs, the except clause is skipped and execution of the try statement is finished.
#If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then if its type matches the exception named after the except keyword, the except clause is executed,

try:
    file = open("test.txt", "r")
    file.write("This is the write command")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    file.close()
