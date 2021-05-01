import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
        name="cmc_csci046_data_structure_Pothis",
        version="1.0.0",
        description="Data Structure and unicode",
        long_description=README,
        url="https://github.com/Tonnpo/csci-046",
        author="Ton Pothisawang",
        author_email="Tonn_po@hotmail.com",
        license="BSD3",
        packages=[ "containers" ]
    )
