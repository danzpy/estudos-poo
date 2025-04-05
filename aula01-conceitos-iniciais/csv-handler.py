class CsvHandler():
    def __init__(self, directory):
        self.dir = directory

    def insert_data_in_csv(self, data):
        print(f'Inserindo {data} em {self.dir}')

    def read_data(self):
        print(f"Lendo dados em {self.dir}")


handle = CsvHandler('/documents/user/file.csv')

handle.insert_data_in_csv('linha 1')
handle.read_data()