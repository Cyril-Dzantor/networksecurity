from typing import List
from setuptools import setup, find_packages

def get_requirements():
    """
    This function will return the list of requirements 

    """
    requirement_list:List[str] = [] 
    try:
        with open ('requirements.txt','r') as file:
            lines = file.readlines()

            for line in lines:
                requirement = line.strip()
                if requirement and requirement != "-e .":
                    requirement_list.append(requirement)
    except:
        print("Requirements.txt file not found")

    return requirement_list

print(get_requirements())

setup(
    name= "NetworkSecurity",
    version= "0.0.1",
    author="Cyril Kojo Dzantor",
    description="Network security project",
    packages=find_packages(),
    install_requires= get_requirements()


)