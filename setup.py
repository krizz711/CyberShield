from setuptools import find_packages, setup
from typing import List

def get_requirement()->List[str]:
    """
    this function will return th list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open("req.txt","r", encoding="utf-8") as file:
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if not requirement:
                    continue
                if requirement.startswith("#"):
                    continue
                if requirement in {"-e .", "--editable ."}:
                    continue
                requirement_lst.append(requirement)
    except FileNotFoundError:
        print("file not found")
    
    return requirement_lst



# setting up meta data

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="criss",
    author_email="munalmax777@gmail.com",
    packages=find_packages(),
    install_requires=get_requirement()
)