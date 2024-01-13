# {{ cookiecutter.project_name }}

{{ cookiecutter.short_project_description }}


## Installation
```bash
pip install git+https://github.com/adampirog/{{ cookiecutter.package_slug }}
```

{% if cookiecutter.command_line_interface == "y" %}
## Usage

```bash
{{ cookiecutter.package_slug }} # use --help option for details
```
{% endif %}
