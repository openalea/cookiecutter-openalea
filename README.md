# cookiecutter-python

An template for [OpenAlea](https://openalea.readthedocs.io/en/latest/) packages. It follows the [OpenAlea development guidelines](https://openalea.readthedocs.io/en/latest/development/guidelines.html).

Best used with [cruft](https://cruft.github.io/cruft/)

To use:

        cruft create https://github.com/openalea-incubator/cookiecutter/

Typical workflow:

1. Create a new package using `cruft create https://github.com/openalea-incubator/cookiecutter/`
2. Initiate your git repository: `git init` (needed for `setuptools_scm` to work properly)
3. Install the package in editable mode with dev dependencies: `mamba env create -f conda/environment.yml`
4. Activate the environment: `mamba activate my_project_dev` # Replace `my_project` with your project slug defined in `cookiecutter.json`
5. Implement your package code in the `src/` directory, add your tests in the `tests/` directory, and documentation in the `doc/` directory.
6. Build the documentation: `cd doc && make html`
7. Run tests: `pytest`
