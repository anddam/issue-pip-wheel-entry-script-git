# Steps to reproduce the issue

1. create a new environment
1. activate the environment
1. upgrade pip and install wheel
1. install local package

```
python -m venv test
. ./test/bin/activate
pip install --upgrade pip wheel
pip install --use-feature=in-tree-build .
```

# Expected result

Package mwe gets installed using a wheel.

# Actual result

Command `bdist_wheel` of setuptools fails with error since the dependency mwedep does not carry the entry_script `mwedep`.


