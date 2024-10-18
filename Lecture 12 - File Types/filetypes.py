
with open('test.csv', 'r') as csv_file:
    headers = csv_file.readline().split(';')
    print(headers)




##############################################
# File Read
##############################################
import csv

with open('test.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        print(row)

    headers = next(csv_reader)
    print(headers)
    new_file_info = []
    for row in csv_reader:
        full_info = ''
        for i in range(len(row)):
            if i == 0:
                full_info += f'first_name: {row[i]},'
            elif i == 1:
                full_info += f'last_name: {row[i]},'
            elif i == 2:
                full_info += f'occupation: {row[i]}'

        with open('test.txt', 'a') as new_file:
            new_file.writelines(full_info + '\n')


    csv_dict_reader = csv.DictReader(csv_file, delimiter='\t')
    for row in csv_dict_reader:
        print(row)


##############################################
# File Write
##############################################

import csv

headers = ['first_name', 'last_name', 'occupation']

rows = [
    ['John', 'Smith', 'Engineer'],
    ['Kate', 'Johnson', 'Sales'],
    ['Bob', 'Michelson', 'Developer']
]

with open('data.csv', 'a') as csvfile:
    csv_writer = csv.writer(csvfile)

    csv_writer.writerow(headers)

    csv_writer.writerows(rows)



headers = ['first_name', 'last_name', 'occupation']

rows = [
    {'first_name': 'John', 'last_name': 'Smith', 'occupation': 'Engineer'},
    {'last_name': 'Jonhson', 'first_name': 'Kate'},
    {'last_name': 'Bobson', 'occupation': 'Engineer'},
]

with open('data2.csv', 'w') as csv_file:
    csv_dict_writer = csv.DictWriter(csv_file, delimiter='\t', fieldnames=headers)

    csv_dict_writer.writeheader()

    csv_dict_writer.writerows(rows)



# Index, OrganizationID, Name, Founded - Century

import csv
headers = ['index', 'org_id', 'name', 'century']
new_list = []
with open("organizations-100.csv", 'r') as csvfile:
    csv_dict_reader = csv.DictReader(csvfile, delimiter=',')
    for row in csv_dict_reader:
        info = {'index': row['Index'], 'org_id': row['Organization Id'], 'name': row['Name']}
        if int(row['Founded']) < 2000:
            century = '20-th Century'
        else:
            century = '21-th Century'
        info.setdefault('century', century)
        new_list.append(info)

with open('newOrganizations-100.csv', 'w', newline='') as newFile:
    writer = csv.DictWriter(newFile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(new_list)