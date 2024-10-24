from setuptools import setup, find_packages

setup(
    name='diy-stereovision',
    version='0.1',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'numpy',
        'opencv-python',
        'scipy',
        'matplotlib'
    ],
    author='Your Name',
    author_email='your.email@example.com',
    description='A custom stereovision setup using Python and OpenCV',
    url='https://github.com/your_username/your_repository_name',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
