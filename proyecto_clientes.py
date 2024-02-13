import sys
import csv
import os

CLIENT_TABLE = '.clients.csv'
CLIENT_SCHEMA = ['name', 'company', 'email', 'position']
clients = []


def _initialize_clients_from_storage():
    with open(CLIENT_TABLE, mode='r') as f:
        reader = csv.DictReader(f, fieldnames=CLIENT_SCHEMA)

        for row in reader:
            clients.append(row)


def _save_clients_to_storage():
    tmp_table_name = f'{CLIENT_TABLE}.tmp' # tabla temporal, no se puede editar un archivo mientras se está abierto o leyendo
    with open(tmp_table_name, mode='w') as f:
        writer = csv.DictWriter(f, fieldnames=CLIENT_SCHEMA) # f es como pasarle el archivo a la función
        writer.writerows(clients)

    os.remove(CLIENT_TABLE)
    os.rename(tmp_table_name, CLIENT_TABLE) # renombramos el archivo temporal al nombre de la original


def create_client(client):
    global clients

    if client not in clients:
        clients.append(client)
    else:
        print('Client already is in the client\'s list')


def list_clients():
    for idx, client in enumerate(clients):
        print(f'{idx}: {client['name']} | {client['company']} | {client['email']} | {client['position']}')


def update_client(index, client_name):
    print(f'What is the field you want to update of the client {client_name}?')
    print('[N]ame')
    print('[C]ompany')
    print('[E]mail')
    print('[P]osition')

    field = input()
    field = field.upper()

    if field == 'N':
        clients[index]['name'] = _get_client_field('name')
    elif field == 'C':
        clients[index]['company'] = _get_client_field('company')
    elif field == 'E':
        clients[index]['email'] = _get_client_field('email')
    elif field == 'P':
        clients[index]['position'] = _get_client_field('position')
    else:
        print('Invalid command')


def delete_client(index):
    eliminado = clients.pop(index)
    print(f'Client {eliminado['name']} has been deleted')


def search_client(client_name):
    global clients
    for client in clients:
        if client != client_name:
            continue
        else:
            return True




def _print_welcome():
    print('Welcome to platzi ventas')
    print('*' * 50)
    print('What would you like to do today?')
    print('[C]reate client')
    print('[L]ist clients')
    print('[U]pdate cliente')
    print('[D]elete cliente')
    print('[S]earch client')


def _get_client_field(field):
    client_field = None

    while not client_field:
        client_field = input(f'What is the client {field}?: ')

        if client_field == 'exit':
            client_field = None
            break

    if not client_field:
        sys.exit()

    return client_field


def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('What is the client name?: ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name


def _get_index_client(client_name):
    global clients
    for idx, client in enumerate(clients):
        if client['name'] == client_name:
            return idx
        else:
            print('Client is not in clients list')
    return None







if __name__ == '__main__':
    _initialize_clients_from_storage()
    _print_welcome()

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
        # list_clients()

    elif command == 'L':
        list_clients()

    elif command == 'U':
        client_name = _get_client_name() # Solicitamos el nombre del cliente a actualizar
        index = _get_index_client(client_name) # Buscamos el cliente en la lista y obtenemos su indice
        if index is not None:
            update_client(index, client_name)
            # list_clients()

    elif command == 'D':
        client_name = _get_client_name()
        index = _get_index_client(client_name)
        if index is not None:
            delete_client(index)
            # list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        index = _get_index_client(client_name)

        if index is not None:
            print('The client is in the client\'s list')
            print(f'{clients[index]['name']} | {clients[index]['company']} | {clients[index]['email']} | {clients[index]['position']}')

    else:
        print('Invalid command')
    
    _save_clients_to_storage() # Guardamos los cambios en el archivo csv
