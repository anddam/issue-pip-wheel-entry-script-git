import os
import sys
import subprocess

from setuptools.command.install import install
from setuptools import setup, find_packages
from wheel.bdist_wheel import bdist_wheel


class Install(install):
    def run(self):
        super().run()
        check_external_executable("install")


class BdistWheel(bdist_wheel):
    def run(self):
        super().run()
        check_external_executable("wheel")


def check_external_executable(name):
    print(f"**** check_external_executable({name}) - START", file=sys.stderr)
    executable_dir = os.path.dirname(sys.executable)
    mwedep_path = os.path.join(executable_dir, "mwedep")
    subprocess.check_output([mwedep_path])
    print(f"**** check_external_executable({name}) - END", file=sys.stderr)


example_dir = "/".join(__file__.split("/")[:-1])
setup(
    cmdclass={
        'install': Install,
        'bdist_wheel': BdistWheel,
    },
    name="mwe",
    packages=find_packages(include=["mwe"]),
    setup_requires=[],
    install_requires=[
      f"mwedep @ file://localhost/{example_dir}/mwedep"
    ],
)
