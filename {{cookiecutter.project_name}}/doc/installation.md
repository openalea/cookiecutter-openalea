# Installation

You must use conda environment : <https://docs.conda.io/en/latest/index.html>

## Users

### Create a new environment with {{ cookiecutter.project_name }} installed in there

```bash

mamba create -n {{ cookiecutter.project_name }} -c openalea3 -c conda-forge  openalea.{{ cookiecutter.project_slug }}
mamba activate {{ cookiecutter.project_name }}
```

Install {{ cookiecutter.project_name }} in a existing environment

```bash
mamba install -c openalea3 -c conda-forge openalea.{{ cookiecutter.project_slug }}
```

### (Optional) Test your installation

```bash
mamba install -c conda-forge pytest
git clone https://github.com/openalea/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}/test; pytest
```

## Developers

### Install From source

```bash
# Install dependency with conda
mamba env create -n phm -f conda/environment.yml
mamba activate {{ cookiecutter.project_name }}

# Clone {{ cookiecutter.project_name }} and install
git clone https://github.com/openalea/{{ cookiecutter.project_slug }}.git
cd {{ cookiecutter.project_slug }}
pip install .

# (Optional) Test your installation
cd test; pytest
```
