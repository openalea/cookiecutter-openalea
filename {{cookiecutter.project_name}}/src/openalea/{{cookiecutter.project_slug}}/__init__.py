"""**{{cookiecutter.project_name}}**

{{cookiecutter.description}}
"""

from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("openalea.{{cookiecutter.project_slug}}")
except PackageNotFoundError:
    # package is not installed
    pass
