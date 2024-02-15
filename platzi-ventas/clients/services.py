import csv
from clients.models import Client


class Client_Service():
    def __init__(self, table_name):
        self.table_name = table_name

    def create_client(self, client):
        with open(self.table_name, mode='a') as f: # mode='a' para append, para añadir fila (o cliente) al final del archivo
            writer = csv.DictWriter(f, fieldnames=Client.schema())
            writer.writerow(client.to_dict()) # escribe la nueva linea