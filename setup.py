'''
The setup.py file is an essential part of packageing and distributing python projects.It is used by setuptools(or distutils in older pytthon versions)
to define the configuration of your project,such as its metadata,dependencies,and more
'''


from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """This function returns a list of requirements from requirements.txt."""
    requirement_lst: List[str] = []
    try:
        with open('requirements.txt', 'r') as file:
            for line in file:
                requirement = line.strip()
                # Ignore empty lines and '-e .'
                if requirement and requirement != '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst  # DO NOT call get_requirements() inside itself

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Rahul yadav",
    author_email="rahilbhai7320021@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()  # fixed typo here
)
