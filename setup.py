# local packages

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_list:List[str] = []
    
    try:
        with open('requirements.txt', 'r') as file:
            for line in file:
                # Remove inline comments and whitespace
                requirement = line.split('#')[0].strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    
        
    return requirement_list
print(get_requirements())

setup(
    name="AI-TRAVEL-PLANNER",
    version="0.0.1",
    author="sunny savita",
    author_email="snshrivas3365@gmail.com",
    packages = find_packages(),
    install_requires=get_requirements()
)