import re
import sys


MODULE_REGEX = r"^[_a-zA-Z][_a-zA-Z0-9]+$"


def check_package_name():
    package_name = "{{ cookiecutter.package_name }}"

    if not re.match(MODULE_REGEX, package_name):
        print(f"ERROR: {package_name} is not a valid Python package name")

        # exits with status 1 to indicate failure
        sys.exit(1)


def main():
    check_package_name()


if __name__ == "__main__":
    main()
