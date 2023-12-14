import subprocess
from pathlib import Path


def remove_cli():
    """
    Remove command line interface if not necessary.
    """
    remove_flag = (
        "{% if cookiecutter.command_line_interface == 'n' %} True {% endif %}"
    )

    if remove_flag:
        cli = Path("{{ cookiecutter.package_name }}") / "__main__.py"
        cli.unlink()


def initialize_repository():
    print("Initializing git repository...")
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "add", "-A"], check=True)
    subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)


def main():
    remove_cli()
    initialize_repository()


if __name__ == "__main__":
    main()
