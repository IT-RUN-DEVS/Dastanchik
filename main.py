import os
import shutil
import datetime
import zipfile


class FileSystem:
    def __init__(self, root_dir):
        self.root_dir = root_dir

    def create(self, file_name):
        file_path = os.path.join(self.root_dir, file_name)
        open(file_path, 'w').close()

    def list(self, dir_path=None):
        dir_path = dir_path or self.root_dir
        return os.listdir(dir_path)

    def copy(self, file_path, dest_dir):
        file_path = os.path.join(self.root_dir, file_path)
        dest_dir = os.path.join(self.root_dir, dest_dir)
        shutil.copy(file_path, dest_dir)

    def move(self, file_path, dest_dir):
        file_path = os.path.join(self.root_dir, file_path)
        dest_dir = os.path.join(self.root_dir, dest_dir)
        shutil.move(file_path, dest_dir)

    def init_fs(self):
        if not os.path.exists('.init_fs'):
            os.makedirs('.init_fs')

    def snapshot(self):
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        snapshot_dir = os.path.join(self.root_dir, f"snapshot_{now}")
        shutil.copytree(self.root_dir, snapshot_dir)

    def backup(self, backup_dir):
        backup_file = os.path.join(self.root_dir, backup_dir + ".zip")
        with zipfile.ZipFile(backup_file, mode="w") as backup_zip:
            for root, dirs, files in os.walk(self.root_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, self.root_dir)
                    backup_zip.write(file_path, arcname=rel_path)
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        backup_dest = os.path.join(desktop, backup_dir + ".zip")
        shutil.move(backup_file, backup_dest)
        print(f"Backup saved to {backup_dest}")


if __name__ == "__main__":
    fs = FileSystem('.')

    while True:
        command = input('command? ').strip()
        if command == "create":
            fs.create(input('Input your file name:'))
            print('Your file is created !')
        elif command == 'list':
            files = fs.list()
            for file in files:
                print(file)
        elif command == 'copy':
            file_path = input('Enter the file path: ')
            dest_dir = input('Enter the destination directory: ')
            fs.copy(file_path, dest_dir)
            print('Copying completed')
        elif command == 'move':
            file_path = input('Enter the file path: ')
            dest_dir = input('Enter the destination directory: ')
            fs.move(file_path, dest_dir)
            print(f'The file "{file_path}" has been moved to "{dest_dir}"')
        elif command == 'init':
            fs.init_fs()
            print('File system initialized!')
        elif command == 'snapshot':
            fs.snapshot()
            print('A snapshot has been created!')
        elif command == 'backup':
            backup_dir = input('Enter the backup directory name: ')
            fs.backup(backup_dir)
            print(f'A backup has been created in "{backup_dir}"!')
        elif command == 'quit':
            break
        else:
            print('Invalid command. Please try again.')

