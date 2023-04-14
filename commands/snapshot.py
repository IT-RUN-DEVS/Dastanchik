import subprocess


def snapshot(dir_from, dir_to):
    try:
        command = ['rsync', '-a', '--exclude', '--delete', dir_from, dir_to]
        process = subprocess.Popen(command)
        process.communicate()
        if process.returncode == 0:
            print("Снимок успешно создан!")
    except Exception as e:
        print("Произошла ошибка при создании снимка: {}".format(str(e)))

