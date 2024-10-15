
file = open('/home/irakli/Desktop/test.py', 'x')

print(file.readable())
print(file.writable())

#################################################
# Read File
#################################################

readable_file = open('test.txt', 'r')

print(readable_file.readable())
read_f = readable_file.read()
print(type(read_f))
print(read_f.upper())

print(readable_file.readline())
print(readable_file.readline())
print(readable_file.readline())
print(readable_file.readlines())
for line in readable_file.readlines():
    info = line.split(',')
    print(f'name: {info[0]}, last_name: {info[1]}')

print(readable_file.closed)
readable_file.close()
print(readable_file.closed)


#################################################
# Write File
#################################################

writable_file = open('writable_file.txt', 'w') # r+ for Read/Write
print(writable_file.read())
print(writable_file.readable())
print(writable_file.writable())

writable_file.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque quis leo vehicula mauris dignissim faucibus. Quisque sollicitudin faucibus leo, sed ornare dolor eleifend in. Nullam ante est, dictum et diam sit amet, consequat aliquet nulla. Cras arcu felis, euismod quis elit id, pharetra varius diam. Etiam fringilla felis mi, sit amet maximus diam suscipit a. Fusce euismod erat eros, at mattis enim aliquam imperdiet. Suspendisse nec placerat odio. Mauris eros ipsum, lobortis eget dui et, rutrum sagittis eros. Nam efficitur tincidunt eros, quis vehicula elit molestie a. Fusce lectus risus, pharetra fringilla convallis a, cursus a metus. Cras aliquet massa eu turpis congue ultrices ornare non ipsum. Mauris mollis dictum odio imperdiet convallis. Nam dictum quam iaculis aliquam elementum. Proin eleifend iaculis ligula, ultrices tincidunt turpis ultricies eget.\n Duis id imperdiet neque.Maecenas tincidunt venenatis tempor. Quisque quis risus at arcu accumsan ullamcorper. Phasellus ut lectus ex. Suspendisse aliquam elit nisi, vitae bibendum ligula luctus eu. Sed at dui pulvinar, tincidunt est quis, dapibus enim. Vivamus at purus a nunc aliquet elementum nec eu velit. In ac finibus arcu. Nullam orci mauris, feugiat non efficitur eu, malesuada vel sem. Mauris convallis urna in rutrum aliquam. Aenean at risus varius magna consectetur accumsan.')
writable_file.write(100) # TypeError


txt_lst = ['irakli,tabatadze\n', 'John,Doe\n', 'James,Johnson\n', 'Kate,Smith']

writable_file.writelines(txt_lst)

writable_file.close()


#################################################
# Append File
#################################################

writable_file = open('writable_file.txt', 'a')

txt_lst = ['irakli,tabatadze\n', 'John,Doe\n', 'James,Johnson\n', 'Kate,Smith\n']

writable_file.writelines(txt_lst)

writable_file.close()



#################################################
# Context Manager
#################################################

with open('test.txt', 'r') as file:
    read_file = file.readlines()

    with open('new_file.txt', 'w') as writable_file:
        writable_file.writelines(read_file)
    print(writable_file.closed)


print(file.closed)

#################################################
# OS Module
#################################################

import os

print(os.listdir())
print(os.mkdir('testDirectory'))
with open('testDirectory/new_test1.txt', 'x'):
    print('File Created')

os.remove('testDirectory/new_test1.txt')
