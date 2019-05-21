import os
print(os.name)
print(os.getcwd())
print(os.getgid())
print(os.getuid())

print(os.path.basename('PyCharmProjects/PythonPrograms'))
print(os.path.dirname('PyCharmProjects/PythonPrograms'))
print(os.path.isabs('/PyCharmProjects/PythonPrograms'))
print(os.path.isdir('/usr'))
print(os.path.normcase('/usr'))
print(os.path.normpath('/PyCharmProjects/./PythonPrograms'))
print(os.path.abspath('/PyCharmProjects/./PythonPrograms'))

'''try:
    # If the file does not exist,
    # then it would throw an IOError
    filename = 'GFG.txt'
    f = open(filename, 'rU')
    text = f.read()
    f.close()

# Control jumps directly to here if
# any of the above lines throws IOError.
except IOError:

    # print(os.error) will <class 'OSError'>
    print('Problem reading: ' + filename)'''


fd = "GFG.txt"

# popen() is similar to open()
'''file = open(fd, 'w')
file.write("Hello")
file.close()
file = open(fd, 'r')
text = file.read()
print(text)

# popen() provides a pipe/gateway and accesses the file directly
file = os.popen(fd, 'w')
file.write("Hello")'''

'''file = open(fd, 'r')
text = file.read()
print(text)
file.close()'''
#os.rename(fd, 'New.txt')

print(os.environ)