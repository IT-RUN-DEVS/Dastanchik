import argparse
import importlib
import os


def main():
    commands_dir = os.path.join(os.path.dirname(__file__), 'commands')
    command_files = [
        os.path.splitext(f)[0] for f in os.listdir(commands_dir)
        if os.path.isfile(os.path.join(commands_dir, f)) and f.endswith('.py')
    ]

    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=command_files)
    parser.add_argument("args", nargs="*")
    args = parser.parse_args()

    module_name = f"commands.{args.command}"
    module = importlib.import_module(module_name)

    getattr(module, args.command)(*args.args)


if __name__ == "__main__":
    main()
