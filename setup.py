from setuptools import find_packages, setup

setup(name='command-line-parsing-in-python',
      version='1.0',
      description='Command Line Parsing in Python Examples',
      author='Adam Englander',
      license="MIT",
      url='https://github.com/aenglander/command-line-parsing-in-python',
      packages=find_packages(),
      setup_requires=['click==6.7', 'cliff==2.9.1'],
      entry_points={
          # This is the console script to be executed
          'console_scripts': [
              'argparse-hello-example = examples.argparse:hello',
              'argparse-goodbye-example = examples.argparse:goodbye',
              'click-example = examples.click:main',
              'cliff-example = examples.cliff:main'
          ],
          'cliff.example': [
              'hello = examples.cliff:Hello',
              'goodbye = examples.cliff:Goodbye'
          ]
      })
