import csv
from utilities.hashTable import HashTable

with open('static/packages.csv') as csvfile:
    file = csv.reader(csvfile, delimiter=',')

    data_to_hash = HashTable()  # creates new HashTable
    # Initialize lists for each truck, as well as return trips for trucks
    truck1 = []
    truck2 = []
    truck1_new_load = []

    # convert csv data into key value pairs, which are loaded into HashTable. Complexity O(N)
    for row in file:
        row_package_ID = row[0]
        location = ''
        row_address = row[1]
        row_city = row[2]
        row_state = row[3]
        row_zip = row[4]
        row_delivery = row[5]
        row_size = row[6]
        row_note = row[7]
        start_delivery = ''
        package_status = 'Hub'
        value = [row_package_ID, location, row_address, row_city, row_state, row_zip, row_delivery, row_size,
                           row_note, start_delivery, package_status]

        # organize packages into their corresponding trucks based on delivery criteria. Attribute values are loaded into
        # a nested list.
        if value[6] != 'EOD':
            if 'Must' in value[8] or 'Null' in value[8]:
                truck1.append(value)
        if 'Can only be' in value[8]:
            truck2.append(value)
        if 'Delayed' in value[8]:
            truck2.append(value)
        if '84104' in value[5] and '10:30' not in value[6]:
            truck1_new_load.append(value)
        if 'Wrong address listed' in value[8]:
            value[2] = '410 S State St'
            value[5] = '84111'
            truck1_new_load.append(value)
        if value not in truck1 and value not in truck2 and value not in truck1_new_load:
            if len(truck1_new_load) < len(truck2):
                truck1_new_load.append(value)
            else:
                truck2.append(value)
        data_to_hash.insert(row_package_ID, value)

    # getter to return full package list. Complexity is O(1)
    def get_package_list():
        return data_to_hash

    # getters to return contents of each truck load. Complexity of each is o(1)
    def get_truck1():
        return truck1

    def get_truck2():
        return truck2

    def get_truck1_new_load():
        return truck1_new_load
