'''
The setup.py file is essential part of packaging and distributing Python projects. It is used by setuptools(or distutils in older Python Versions) to define the configuration of your projects, such as meta data, dependencies and more.
'''

from setuptools import find_packages,setup

'''
find packages will consider the __init__.py and consider taht particular folder containing __init__.py files as a package.

setup provides information about our project.
'''

from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    
    """
    requirement_list:List[str] = []

    try:
        with open('requirements.txt','r') as file:
            # Read lines from the file
            lines = file.readlines()
            # Process each line

            for line in lines:
                requirement = line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement != '-e .':      ### -e. file refers to this setup.py file
                    requirement_list.append(requirement)

    except FileNotFoundError:
        print("requirements.txt not found")
    
    return requirement_list

setup(
    name="NetworkSecurity",
    version="0.0.1",
    autrhor='Manan Singh Panwar',
    author_email = "mananpanwar600@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()

)