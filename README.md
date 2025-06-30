# cookiecutter-openalea

An template for [OpenAlea](https://openalea.readthedocs.io/en/latest/) packages. It follows the [OpenAlea development guidelines](https://openalea.readthedocs.io/en/latest/development/guidelines.html), and provides all necessary files and configurations to develop a new package up to the continuous integration and package publication on a conda channel.

Best used with [cruft](https://cruft.github.io/cruft/)

To use:

        cruft create https://github.com/openalea-incubator/cookiecutter/

## Features

- **Package organization**: Follows the [OpenAlea layout and namespace managment](https://openalea.readthedocs.io/en/latest/development/guidelines.html#package-layout-and-namespace) with `src/openalea`, `tests/`, and `doc/` directories. It also provides [homogeneous package description files](https://openalea.readthedocs.io/en/latest/development/guidelines.html#readme-md) (`README.md`, `LICENSE`, `CODE_OF_CONDUCT.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, etc.).
- **Unified package management and meta-informations** : [`pyproject.toml`](https://openalea.readthedocs.io/en/latest/development/guidelines.html#pyproject-toml) is preconfigured with `setuptools`, `setuptools_scm`, and provides all the necessary sections for filling in your package metadata, dependencies, and development tools. It is also used for filling your conda recipe for building your package.
- **Documentation**: Uses [Sphinx](https://www.sphinx-doc.org/en/master/) for documentation, with a preconfigured `conf.py` and `Makefile`. Layout of the documentation is homogeneous among OpenAlea packages.
- **Continuous integration**: [Preconfigured GitHub Actions](https://openalea.readthedocs.io/en/latest/development/guidelines.html#pyproject-toml) to build and test your package on multiple Python versions, and multiple OS, in a standardized way defined by the [dedicated `Github Actions`](https://github.com/openalea/action-build-publish-anaconda/blob/main/doc/workflows/openalea_ci/README.md)

## Typical workflow

1. Create a new package using `cruft create https://github.com/openalea-incubator/cookiecutter/`
2. Initiate your git repository: `git init` (needed for `setuptools_scm` to work properly)
3. Install the package in editable mode with dev dependencies: `mamba env create -f conda/environment.yml`
4. Activate the environment: `mamba activate my_project_dev` # Replace `my_project` with your project slug defined in `cookiecutter.json`
5. Implement your package code in the `src/` directory, add your tests in the `tests/` directory, and documentation in the `doc/` directory.
6. Build the documentation: `cd doc && make html`
7. Run tests: `pytest`
