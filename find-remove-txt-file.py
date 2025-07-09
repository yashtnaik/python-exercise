import os, os

path=os.getcwd()

for file in os.listdir(path):
    if file.endswith('.txt'):
        print(f'{file} identified and proceeding to delete')
        try:
            os.remove(file)
            print(f'Success {file} deleted')
        except Exception as e:
            print(f'failed to delete {file}: {e}')
