from setuptools import setup, find_packages

setup(
    name="mwedep",
    packages=["."],
    entry_points={"console_scripts": ["mwedep = mwedep:cli"]},
)
