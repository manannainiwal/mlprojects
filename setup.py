from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'

def get_requirements(file_path):
    """
    Read requirements from a file and return as a list of strings.
    """
    requirements = []
    try:
        with open(file_path, 'r') as file_obj:
            requirements = [line.strip() for line in file_obj.readlines() if line.strip() and line.strip() != HYPEN_E_DOT]
    except FileNotFoundError:
        print(f"Warning: File '{file_path}' not found. Proceeding with empty requirements.")
    return requirements

setup(
    name='mlprojects',
    version='0.0.1',
    author='Manan',
    author_email='manannainiwal01@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
