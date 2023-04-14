import subprocess
import datetime


def snapshot(dir_from='.', dir_to=None):
    if not dir_to:
        now = datetime.datetime.now()
        dir_to = now.strftime("%d_%H-%M") + "_Snapshot"
    try:
        command = ['rsync', '-a', '--exclude', '--delete', dir_from, dir_to]
        process = subprocess.Popen(command)
        process.communicate()
        if process.returncode == 0:
            print("Snapshot successfully created!")
    except Exception as e:
        print("An error occurred while creating snapshot: {}".format(str(e)))